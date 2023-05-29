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
      <section class='markets--detail--container'>
        <div class='markets--carousel--dblock'>
          <div class="owl-carousel owl-theme">
            {% for postimage in post.postimages.all %}
              <button class='item owl--carousel--item' value="{{ forloop.counter }}">
                <img src="{{ postimage.image.url }}" alt="{{ post.title }}">
              </button>
            {% endfor %}
          </div>
          <a class="owl--carousel--back" href="{% url 'markets:index' %}">
            <i class="bi bi-chevron-left"></i>
          </a>
        </div>

        <div class='markets--carousel--dnone d-none'>
          <div class="owl-carousel owl-theme">
            {% for postimage in post.postimages.all %}
              <button class='item owl--carousel--item' value="{{ forloop.counter }}">
                <img src="{{ postimage.image_first.url }}" alt="{{ post.title }}">
              </button>
            {% endfor %}
          </div>

          <button class='owl--carousel--close'>
            <i class="bi bi-x"></i>
          </button>
        </div>
      </section>
    {% endblock %}

    <script>
      $('.owl-carousel').owlCarousel({
          startPosition: false,
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

<br/>

### JS
- ```javascript
    // 원본사진 캐러셀 비동기 구현
    const carouselDblock = document.querySelector('.markets--carousel--dblock')
    const carouselBtns = document.querySelectorAll('.markets--carousel--dblock .item')
    const carouselDnone = document.querySelector('.markets--carousel--dnone')
    const detailContainer = document.querySelector('.markets--detail--container')
    let owlCarousel = $('.owl-carousel')

    const detailBody = document.querySelector('.markets--detail')

    carouselBtns.forEach((btn) => {
      btn.addEventListener('click', (event) => {
        carouselDblock.classList.add('d-none') 
        carouselDnone.classList.remove('d-none')
        detailContainer.style = 'max-width: 450px;'
        detailBody.style = 'background-color: black;'
          
        const btnValue = btn.value
        owlCarousel.trigger('to.owl.carousel', [btnValue - 1]);
      })
    })


    const closeBtn = document.querySelector('.owl--carousel--close')
    const carouselDnoneItems = document.querySelectorAll('.markets--carousel--dnone .owl-item')

    closeBtn.addEventListener('click', (event) => {
      carouselDblock.classList.remove('d-none')
      carouselDnone.classList.add('d-none')
      detailContainer.style = ''
      detailBody.style = 'background-color: white;'

      carouselDnoneItems.forEach((item) => {
        if (item.classList.contains('active')) {
          itemValue = item.querySelector('button').value
        }
      })

      owlCarousel.trigger('to.owl.carousel', [itemValue - 1]);
    })
  ```

