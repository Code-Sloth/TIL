# Hash Change JS

<br/>

### html
- ```html
    <div class='section-container d-flex'>

      <a class='section-header-a section-js-top' href="{% url 'courses:detail' course.pk %}#top">
        강의소개
      </a>

      <a class='section-header-a section-js-reviews ps-1' href="{% url 'courses:detail' course.pk %}#reviews">
        수강평<span>{{ course.reviews.count }}</span>
      </a>

      <a class='section-header-a {% if comment_type %}course-detail-black{% endif %}' href="{% url 'courses:comment' course.pk %}?type=qna">
        커뮤니티
      </a>
    </div>
  ```

<br/>

### JS
- ```javascript
    const detailATop = document.querySelector('.section-js-top')
    const detailAReviews = document.querySelector('.section-js-reviews')

    function handleHashChange() {
      const currentHash = window.location.hash

      detailATop.classList.remove('course-detail-black')
      detailAReviews.classList.remove('course-detail-black')

      if (currentHash === '#top') {
        detailATop.classList.add('course-detail-black')
      } else if (currentHash === '#reviews') {
        detailAReviews.classList.add('course-detail-black')
      }
    }

    window.addEventListener('hashchange', handleHashChange)

    const currentHash = window.location.hash

    detailATop.classList.remove('course-detail-black')
    detailAReviews.classList.remove('course-detail-black')

    if (currentHash === '#top') {
      detailATop.classList.add('course-detail-black')
    } else if (currentHash === '#reviews') {
      detailAReviews.classList.add('course-detail-black')
    }
  ```