# 별점

<br/>

## 총 별점 출력
- ```python
    @property
    def star_multiple(self):
        return self.star*20
  ```
  ```html
    <div class='star-box comment-starbox'>
      <div class='star-gray'>
        <img class='w-100' src="{% static 'image/product_graystar.png' %}" alt="graystar">
      </div>
      <div class='star-star comment-star-star' style='width: {{ comment.star_multiple }}%;'>
        <img src="{% static 'image/product_star.png' %}" alt="star">
      </div>
    </div>
  ```
  ```css
    .star-box {
      position: relative;
      width: 140px;
    }

    .star-star {
      position: absolute;
      top: 0;
      overflow: hidden;
    }
  ```

### 별점 저장
- ```python
    def detail(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    comments = product.comment_set.all()

    if comments:
        star_sum = sum([comment.star for comment in comments])
        star_avg = star_sum / comments.count()
        product.star = round(star_avg,1)
        product.save()
  ```

### 별점 create
- ```html
    <form action="{% url 'products:comment_create' product.pk %}" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      <div class='d-flex'>
        <button type="button" class='comment_star' id="star1" data-value="1">
          <img src="{% static 'img/orange_star.png' %}" id="img1" alt="orangestar" data-value="1">
        </button>
        <button type="button" class='comment_star' id="star2" data-value="2">
          <img src="{% static 'img/orange_star.png' %}" id="img2" alt="orangestar" data-value="2">
        </button>
        <button type="button" class='comment_star' id="star3" data-value="3">
          <img src="{% static 'img/orange_star.png' %}" id="img3" alt="orangestar" data-value="3">
        </button>
        <button type="button" class='comment_star' id="star4" data-value="4">
          <img src="{% static 'img/orange_star.png' %}" id="img4" alt="orangestar" data-value="4">
        </button>
        <button type="button" class='comment_star' id="star5" data-value="5">
          <img src="{% static 'img/orange_star.png' %}" id="img5" alt="orangestar" data-value="5">
        </button>
      </div>
      {{ comment_form.as_p }}
      {{ commentimage_form.as_p }}

      <button id="star_rating" name="star_rating" value="5" type="submit">리뷰 작성</button>
    </form>
  ```
  ```javascript
    document.addEventListener('DOMContentLoaded', () => {
      const starBtns = document.querySelectorAll('.comment_star');
      const starRating = document.querySelector('#star_rating');
      starBtns.forEach((btn) => {
        btn.addEventListener('click', (event) => {
          const value = event.target.getAttribute('data-value');

          starRating.value = value;
          starBtns.forEach((btn) => {
            const img = btn.querySelector('img');
            const attr = btn.getAttribute('data-value')
            console.log(attr)
            if (attr <= value) {
              img.src = "/static/img/orange_star.png";
              img.alt = "orange_star"
            } else {
              img.src = "/static/img/gray_star.png";
              img.alt = "gray_star"
            }
          });
        });
      });
    });
  ```
