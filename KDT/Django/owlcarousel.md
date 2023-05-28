# OwlCarousel

<br/>

### 다운로드
- [OwlCarousel](https://owlcarousel2.github.io/OwlCarousel2/)
- docs/assets/vendors/jquery.min.js
- dist/owl.carousel.js
- dist/assets/owl.carousel.css
- dist/assets/owl.theme.default.min.css

<br/>

### html
- ```html
    <!-- jquery.min.js가 맨 위로 와야 함 -->
    <script src="{% static 'owlcarousel/jquery.min.js' %}"></script>
    <link rel="stylesheet" href="{% static 'owlcarousel/owl.carousel.css' %}">
    <link rel="stylesheet" href="{% static 'owlcarousel/owl.theme.default.min.css' %}">
    <script src="{% static 'owlcarousel/owl.carousel.js' %}"></script>

    {% block content %}
      <div class="owl-carousel owl-theme">
        {% for postimage in post.postimages.all %}
          <div class='item'>
            <img src="{{ postimage.image.url }}" alt="{{ post.title }}">
          </div>
        {% endfor %}
      </div>
    {% endblock %}

    <script>
      $('.owl-carousel').owlCarousel({
          loop:true,
          margin:10,
          responsiveClass:true,
          responsive:{
              0:{
                  items:1,
                  nav:true
              },
              600:{
                  items:1,
                  nav:false
              },
              1000:{
                  items:1,
                  nav:true,
                  loop:false
              }
          }
      })
    </script>
  ```
