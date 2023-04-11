# 장고 게시판

<br/>

## form의 css관리
- ```python
    # forms.py

    from django import forms
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
    from django.contrib.auth import get_user_model

    class CustomUserCreationForm(UserCreationForm):
        # 첫 번째 방법
        birthday = forms.DateField(
            label = '생년 월일:',
            widget=forms.DateInput(attrs={'type':'date'})
            )
        
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
            fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2','birthday')

        # 두 번째 방법
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = '아이디' 
  ```

<br/>

## 정렬
- ```html
    <!-- index.html -->

    <form class='form__sort' action="{% block index__url %}{% url 'posts:index' %}{% endblock index__url %}">
      <input {% if sor == '최신순' %}class='text-warning'{% endif %} type="submit" name='sort' value='최신순'>
      <input {% if sor == '오래된순' %}class='text-warning'{% endif %} type="submit" name='sort' value='오래된순'>
      <input {% if sor == '조회순' %}class='text-warning'{% endif %} type="submit" name='sort' value='조회순'>
      <input {% if sor == '추천순' %}class='text-warning'{% endif %} type="submit" name='sort' value='추천순'>
    </form>

    <!-- block안에 url을 넣어서 재사용성을 높임 -->
    <!-- sor의 값을 받아와 if문을 통해 선택하고 나서 뭘 선택했는지 표시가 남아있게 함 -->
    <!-- form으로 name이 sort이고 value값을 다르게 해서 해당 url로 전달 -->
    <!-- 누르자마자 전달해야하기 때문에 input의 type을 submit으로 설정 -->

    <!-- 태그 안에 다른 값을 넣고싶으면 button으로 바꿔도 가능 -->
    <form action="{% url 'posts:detail' post.pk %}" method="POST">
      {% csrf_token %}
      <button class='btn' type='submit' name='like' value='unlike'>
        <svg width='20px' height='20px' xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" class="hover:text-red-500 group-hover:text-red-500 h-4 w-4"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"></path></svg>
      </button>
    </form>
  ```
- ```python
    # views.py

    def index(request):
      posts = Post.objects.all()
      sor = request.GET.get('sort','')
      posts = sort_func(posts,sor)
      return render(request, 'posts/index.html',{'posts':posts,'sor':sor})
    
    # sor로 html에서 보낸 name이 sort인 value값을 저장
    # posts에 sort_func의 리턴값을 저장

    def sort_func(queryset, so):
      if so == '최신순':
          return queryset.order_by('-pk')
      elif so == '오래된순':
          return queryset.order_by('pk')
      elif so == '조회순':
          return queryset.order_by('-count_hit')
      elif so == '추천순':
          return queryset.order_by('-count_like')
      else:
          return queryset[::-1]

    # 조건문을 통해 그에 맞는 값의 기준으로 정렬을 수행해서 리턴
    # 아무값도 받지 않으면 else로 빠져서 최신 글이 위로 올라오도록 리턴
  ```

<br/>

## 게시글 등록일 표시
- app내에 templatetags 폴더 생성
- templatetags 안에 __ init__.py 파일 생성
- templatetags 안에 filters.py 파일 생성
- ```python
    # templatetags/filters.py

    from django import template
    # datetime안의 timezone은 시간대 처리를 위한 내장 지원 기능은 없기 때문에 추가 기능을 제공하는 django.utils에서 timezone모듈을 가져옴
    from django.utils import timezone
    from datetime import timedelta

    # 사용자 정의 템플릿 태그를 만들어서 django 템플릿인 html에서도 이 함수들을 사용할 수 있게 만들어 줌
    register = template.Library()

    def format_time_since(value):
        now = timezone.now()

        diff = now - value
        # now와 value의 시간 차이가 1분 차이 미만이면
        if diff < timedelta(minutes=1):
            return f'방금 전'
        # now와 value의 시간 차이가 1시간 차이 미만이면
        elif diff < timedelta(hours=1):
            return f'{diff.seconds // 60}분 전'
        # now와 value의 시간 차이가 1일 차이 미만이면
        elif diff < timedelta(days=1):
            return f'{diff.seconds // 3600}시간 전'
        else:
            # python의 datetime모듈에 있는 메서드로 날짜를 문자열로 반환해줌
            return value.strftime('%Y-%m-%d')

    # 템플릿 엔진이 템플릿에서 이 필터를 만나면 위의 함수를 호출
    register.filter('format_time_since', format_time_since)
  ```
- ```html
    <!-- index.html -->

    {% load filters %} <!-- templatetags폴더 안에 생성한 파일 이름으로 호출 -->

    {{ post.created_time|format_time_since }} <!-- filters.py안의 함수를 호출해 리턴을 받음 -->
  ```
