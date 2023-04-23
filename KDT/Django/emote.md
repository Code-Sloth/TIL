# Emote

<br/>

## Emote 기능 구현
- ```python
    # articles/models.py

    class Article(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        emote_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='emote_articles', through='Emote')
        title = models.CharField(max_length=80)
        content = models.TextField(null=False)


    class Comment(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        emote_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='emote_comments', through='CommentEmote')
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
        content = models.TextField(null=False)

    class Emote(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        emotion = models.CharField(max_length=20)

    class CommentEmote(models.Model):
        comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        emotion = models.CharField(max_length=20)
  ```
  ```python
    # articles/views.py

    EMOTIONS = [
        {'label': '쓸쓸정보', 'value': 1},
        {'label': '흥미진진', 'value': 2},
        {'label': '공감백배', 'value': 3},
        {'label': '분석탁월', 'value': 4},
        {'label': '후속강추', 'value': 5},
    ]

    COMMENT_EMOTIONS = [
        {'label': '좋아요', 'value': 1},
        {'label': '싫어요', 'value': 2},
    ]


    def detail(request, article_pk):
        article = Article.objects.get(pk=article_pk)

        emotions = []
        for emotion in EMOTIONS:
            label = emotion['label']
            value = emotion['value']
            count = Emote.objects.filter(article=article, emotion=value).count()
            if request.user.is_authenticated:
                exist = Emote.objects.filter(article=article, emotion=value, user=request.user)
            else: exist = None
            emotions.append(
                {
                    'label': label,
                    'value': value,
                    'count': count,
                    'exist': exist,
                }
            )
            
        comments = article.comment_set.all()
        comment_emotions = {}
        for comment in comments:
            comment_emotions[comment.pk] = []
            for comment_emotion in COMMENT_EMOTIONS:
                label = comment_emotion['label']
                value = comment_emotion['value']
                count = CommentEmote.objects.filter(comment=comment, emotion=value).count()
                if request.user.is_authenticated:
                    exist = CommentEmote.objects.filter(comment=comment, emotion=value, user=request.user)
                else: exist = None
                comment_emotions[comment.pk].append(
                    {
                        'label': label,
                        'value': value,
                        'count': count,
                        'exist': exist,
                    }
                )

        comment_form = CommentForm()
        context = {
            'emotions': emotions,
            'comment_emotions': comment_emotions,
            'article': article,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(request, 'articles/detail.html', context)


    @login_required
    def emotes(request, article_pk, emotion):
        article = Article.objects.get(pk=article_pk)
        filter_query = Emote.objects.filter(
            article=article,
            user=request.user,
            emotion=emotion,
        )
        if filter_query.exists():
            filter_query.delete()
        else:
            Emote.objects.create(article=article, user=request.user, emotion=emotion)

        return redirect('articles:detail', article_pk)

    @login_required
    def comment_emotes(request, article_pk, comment_pk, comment_emotion):
        comment = Comment.objects.get(pk=comment_pk)
        filter_query = CommentEmote.objects.filter(
            comment=comment,
            user=request.user,
            emotion=comment_emotion,
        )
        if filter_query.exists():
            filter_query.delete()
        else:
            CommentEmote.objects.create(comment=comment, user=request.user, emotion=comment_emotion)

        return redirect('articles:detail', article_pk)
  ```
  ```html
    <!-- articles/detail.html -->

    <!-- 게시글 이모션 -->

    <div class='d-flex justify-content-around mx-auto' style='width:75%;'>
      {% for emotion in emotions %}
        <div>
          {% if request.user.is_authenticated %}
          {{emotion.queryset}}
            <form action="{% url 'articles:emotes' article.pk emotion.value %}" method="POST">
              {% csrf_token %}
                {% if emotion.exist %}
                  <button class="img0 img{{emotion.value}} emo" type="submit">
                    <div class="btn-click">{{ emotion.label }}</div>
                  </button>
                {% else %}
                  <button class="img0 img{{emotion.value}} emo" type="submit">
                    <div class="btn-unclick">{{ emotion.label }}</div>
                  </button>
                {% endif %}
            </form>
          {% else %}
            <button disabled="disabled">{{emotion.label}}</button>
          {% endif %}
          <p class='ms-3 {% if emotion.exist %}btn-click{% else %}btn-unclick{% endif %}'>
            {{ emotion.count }}
          </p>
        </div>
      {% endfor %}
    </div>

    <!-- 댓글 이모션 -->

    {% for comment in comments %}
      <div class='d-flex justify-content-between'>
        <p>
          {{comment.user}} : {{comment.content}}
        </p>

        <div class='d-flex'>
          {% for comment_pk, comment_emo in comment_emotions.items%}
            {% if comment_pk == comment.pk %}
              {% for comment_emotion in comment_emo %}
                <div>
                  {% if request.user.is_authenticated %}
                  {{comment_emotion.queryset}}
                    <form class='d-flex align-items-center justify-content-between me-2 pt-2' style="width:30px;" action="{% url 'articles:comment_emotes' article.pk comment.pk comment_emotion.value %}" method="POST">
                      {% csrf_token %}
                      {% if comment_emotion.exist %}
                        <button class="like0 like{{ comment_emotion.value }} like{{ comment_emotion.value }}{{ comment_emotion.value }}" type="submit">
                        </button>
                        <div class="fw-bold">
                          {{ comment_emotion.count }}
                        </div>
                      {% else %}
                        <button class="like0 like{{ comment_emotion.value }}" type="submit">
                        </button>
                        {{ comment_emotion.count }}
                      {% endif %}
                    </form>
                  {% else %}
                    <button disabled="disabled">{{comment_emotion.label}}</button>
                  {% endif %}
                </div>
              {% endfor %}
            {% endif %}
          {% endfor %}
        </div>
      </div>
  {% endfor %}
  ```