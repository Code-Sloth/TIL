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

### 별점 저장 및 삭제
- ```python
    # models.py/Comments model
    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        total_star = 0
        for comment in self.product.comments.all():
            total_star += comment.star

        if self.product.comments.count() >= 1:
            self.product.star = total_star / self.product.comments.count()
        else:
            self.product.star = 0
 
        self.product.save()

    def delete(self, *args, **kargs):
        super(Comment, self).delete(*args, **kargs)
        total_star = 0
        for comment in self.product.comments.all():
            total_star += comment.star

        if self.product.comments.count() >= 1:
            self.product.star = total_star / self.product.comments.count()
        else:
            self.product.star = 0

        self.product.save()
  ```

### 별점 create
- ```html
    <form action="{% url 'products:comment_create' product.pk %}" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      <div class='d-flex'>
        <button type="button" class='comment_star' id="star1" data-value="1">
          <img src="{% static 'image/star1.svg' %}" id="img1" alt="star" data-value="1">
        </button>
        <button type="button" class='comment_star' id="star2" data-value="2">
          <img src="{% static 'image/star1.svg' %}" id="img2" alt="star" data-value="2">
        </button>
        <button type="button" class='comment_star' id="star3" data-value="3">
          <img src="{% static 'image/star1.svg' %}" id="img3" alt="star" data-value="3">
        </button>
        <button type="button" class='comment_star' id="star4" data-value="4">
          <img src="{% static 'image/star1.svg' %}" id="img4" alt="star" data-value="4">
        </button>
        <button type="button" class='comment_star' id="star5" data-value="5">
          <img src="{% static 'image/star1.svg' %}" id="img5" alt="star" data-value="5">
        </button>
      </div>
      {{ comment_form.content }}
      {{ comment_form.image }}

      <button id='star_rating' name='star_rating' value='5' class='btn btn-primary w-100 mt-5 mb-3' type='submit'>등록</button>
    </form>
  ```
  ```javascript
    document.addEventListener('DOMContentLoaded', () => {
      const starBtns = document.querySelectorAll('.comment_star')
      const starRating = document.querySelector('#star_rating')
      const starContent = document.querySelector('.comment-star-content')

      starBtns.forEach((btn) => {
        btn.addEventListener('click', (event) => {
          const value = event.target.getAttribute('data-value')

          if (value == 1) {
            starContent.textContent = '나쁨'
          } else if (value == 2) {
            starContent.textContent = '별로'
          } else if (value == 3) {
            starContent.textContent = '보통'
          } else if (value == 4) {
            starContent.textContent = '좋음'
          } else if (value == 5) {
            starContent.textContent = '최고'
          }

          starRating.value = value
          starBtns.forEach((bt) => {
            const img = bt.querySelector('img')
            const attr = bt.getAttribute('data-value')
            console.log(attr)
            if (attr <= value) {
              img.src = "/static/image/star1.svg"
              img.alt = "star1"
            } else {
              img.src = "/static/image/graystar1.svg"
              img.alt = "graystar1"
            }
          })
        })
      })
    })
  ```
