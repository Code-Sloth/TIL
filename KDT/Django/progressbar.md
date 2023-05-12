# 별점 게이지 구현

<br/>

### views.py
- ```python
      def detail(request, course_pk):
      course = Course.objects.get(pk=course_pk)
      reviews = Review.objects.filter(course_id=course_pk)

      star_percentage = []
      if reviews:
          for x in range(1, 6):
              star_percentage.append(round(reviews.filter(star=x).count()*100/reviews.count(), 1))
      else:
          star_percentage = [0, 0, 0, 0, 0]
      context = {
          'course': course,
          'reviews': reviews,
          'review_form': review_form,
          'other_courses': other_courses,
          'similar_courses': similar_courses,
          'star_percentage': star_percentage,
      }
      return render(request, 'courses/course_detail.html', context)
  ```

<br/>

### html
- ```python
    <div class="review-dashboard-graph">

      <div class='review-progressbox'>
        <div class='review-progress-title'>5점</div>
        <div class='review-progress'>
          <div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
            <div class="progress-bar" style="width: {{ star_percentage.4 }}%"></div>
          </div>
        </div>
      </div>

      <div class='review-progressbox'>
        <div class='review-progress-title'>4점</div>
        <div class='review-progress'>
          <div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
            <div class="progress-bar" style="width: {{ star_percentage.3 }}%"></div>
          </div>
        </div>
      </div>

      <div class='review-progressbox'>
        <div class='review-progress-title'>3점</div>
        <div class='review-progress'>
          <div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
            <div class="progress-bar" style="width: {{ star_percentage.2 }}%"></div>
          </div>
        </div>
      </div>

      <div class='review-progressbox'>
        <div class='review-progress-title'>2점</div>
        <div class='review-progress'>
          <div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
            <div class="progress-bar" style="width: {{ star_percentage.1 }}%"></div>
          </div>
        </div>
      </div>

      <div class='review-progressbox'>
        <div class='review-progress-title'>1점</div>
        <div class='review-progress'>
          <div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
            <div class="progress-bar" style="width: {{ star_percentage.0 }}%"></div>
          </div>
        </div>
      </div>

    </div>
  ```