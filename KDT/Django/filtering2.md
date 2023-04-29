# 필터링 구현 2

<br/>

## HTML
- ```html
    {% comment %} 필터링 {% endcomment %}
    <div class='d-flex my-5'>

      {% comment %} 도수 {% endcomment %}
      <div class='filtering-btn' name='dosu'>
        <a class='filtering-a' data-bs-toggle="collapse" href="#multiCollapseExample-dosu" role="button" aria-expanded="false" aria-controls="multiCollapseExample-dosu">
          <div class='filtering-title'>
            <p>도수</p>
          </div>
          <div class='filtering-img'>
            <img class='w-100' src="{% static 'image/down.png' %}" alt="down">
          </div>
        </a>
  
        <div class="filtering-collapse collapse multi-collapse" id="multiCollapseExample-dosu">
          <button class='filtering' name='dosu' value='0,10'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                0%~10%
              </div>
            </div>
          </button>

          <button class='filtering' name='dosu' value='10,20'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                10%~20%
              </div>
            </div>
          </button>

          <button class='filtering' name='dosu' value='20,30'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                20%~30%
              </div>
            </div>
          </button>

          <button class='filtering' name='dosu' value='30,100'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                30%이상
              </div>
            </div>
          </button>

        </div>
      </div>

      {% comment %} 단맛 {% endcomment %}
      <div class='filtering-btn' name='sweet'>
        <a class='filtering-a' data-bs-toggle="collapse" href="#multiCollapseExample-sweet" role="button" aria-expanded="false" aria-controls="multiCollapseExample-sweet">
          <div class='filtering-title'>
            <p>단맛</p>
          </div>
          <div class='filtering-img'>
            <img class='w-100' src="{% static 'image/down.png' %}" alt="down">
          </div>
        </a>
  
        <div class="filtering-collapse collapse multi-collapse" id="multiCollapseExample-sweet">
          <button class='filtering' name='sweet' value='low'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                약한
              </div>
            </div>
          </button>

          <button class='filtering' name='sweet' value='middle'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                중간
              </div>
            </div>
          </button>

          <button class='filtering' name='sweet' value='strong'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                강한
              </div>
            </div>
          </button>

        </div>
      </div>

      {% comment %} 신맛 {% endcomment %}
      <div class='filtering-btn' name='sourness'>
        <a class='filtering-a' data-bs-toggle="collapse" href="#multiCollapseExample-sourness" role="button" aria-expanded="false" aria-controls="multiCollapseExample-sourness">
          <div class='filtering-title'>
            <p>신맛</p>
          </div>
          <div class='filtering-img'>
            <img class='w-100' src="{% static 'image/down.png' %}" alt="down">
          </div>
        </a>
  
        <div class="filtering-collapse collapse multi-collapse" id="multiCollapseExample-sourness">
          <button class='filtering' name='sourness' value='low'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                약한
              </div>
            </div>
          </button>

          <button class='filtering' name='sourness' value='middle'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                중간
              </div>
            </div>
          </button>

          <button class='filtering' name='sourness' value='strong'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                강한
              </div>
            </div>
          </button>

        </div>
      </div>

      {% comment %} 쓴맛 {% endcomment %}
      <div class='filtering-btn' name='bitterness'>
        <a class='filtering-a' data-bs-toggle="collapse" href="#multiCollapseExample-bitterness" role="button" aria-expanded="false" aria-controls="multiCollapseExample-bitterness">
          <div class='filtering-title'>
            <p>쓴맛</p>
          </div>
          <div class='filtering-img'>
            <img class='w-100' src="{% static 'image/down.png' %}" alt="down">
          </div>
        </a>
  
        <div class="filtering-collapse collapse multi-collapse" id="multiCollapseExample-bitterness">
          <button class='filtering' name='bitterness' value='low'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                약한
              </div>
            </div>
          </button>

          <button class='filtering' name='bitterness' value='middle'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                중간
              </div>
            </div>
          </button>

          <button class='filtering' name='bitterness' value='strong'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                강한
              </div>
            </div>
          </button>

        </div>
      </div>

      {% comment %} 탄산 {% endcomment %}
      <div class='filtering-btn' name='carbonated'>
        <a class='filtering-a' data-bs-toggle="collapse" href="#multiCollapseExample-carbonated" role="button" aria-expanded="false" aria-controls="multiCollapseExample-carbonated">
          <div class='filtering-title'>
            <p>탄산</p>
          </div>
          <div class='filtering-img'>
            <img class='w-100' src="{% static 'image/down.png' %}" alt="down">
          </div>
        </a>
  
        <div class="filtering-collapse collapse multi-collapse" id="multiCollapseExample-carbonated">
          <button class='filtering' name='carbonated' value='True'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                있음
              </div>
            </div>
          </button>

          <button class='filtering' name='carbonated' value='False'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                없음
              </div>
            </div>
          </button>

        </div>
      </div>

      {% comment %} 가격 {% endcomment %}
      <div class='filtering-btn' name='price' style='margin:0;'>
        <a class='filtering-a' data-bs-toggle="collapse" href="#multiCollapseExample-price" role="button" aria-expanded="false" aria-controls="multiCollapseExample-price">
          <div class='filtering-title'>
            <p>가격</p>
          </div>
          <div class='filtering-img'>
            <img class='w-100' src="{% static 'image/down.png' %}" alt="down">
          </div>
        </a>
  
        <div class="filtering-collapse collapse multi-collapse" id="multiCollapseExample-price">

          <div class='price-search'>
            <input placeholder="0원" class='price-number1' type="text">
            <span>~</span>
            <input placeholder="100,000원" class='price-number2' type="text">
            <button class='price-search-submit'>적용</button>
          </div>

          <button class='filtering pricing' name='price' value='0,10000'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                ~ 1만원
              </div>
            </div>
          </button>
  
          <button class='filtering pricing' name='price' value='10000,30000'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                1만원 ~ 3만원
              </div>
            </div>
          </button>
  
          <button class='filtering pricing' name='price' value='30000,50000'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                3만원 ~ 5만원
              </div>
            </div>
          </button>
  
          <button class='filtering pricing' name='price' value='50000,100000'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                5만원 ~ 10만원
              </div>
            </div>
          </button>
  
          <button class='filtering pricing' name='price' value='100000,1000000'>
            <div class='filtering-collapse-box'>
              <div class='filtering-check'>
                <img class='w-100' src="{% static 'image/no-check.png' %}" alt="no-check">
              </div>
              <div class='filtering-text'>
                10만원 이상
              </div>
            </div>
          </button>
  
        </div>
      </div>

    </div>
  ```

<br/>

## JavaScript
- ```javascript
    // 콜랩스 색깔, 이미지 변환
    const filterBtns = document.querySelectorAll('.filtering-btn')

    filterBtns.forEach((btn) => {
      const btnName = btn.getAttribute('name')
      const btnTitle = btn.querySelector('.filtering-title > p')
      const Url = window.location.href
      const filters = btn.querySelectorAll('.filtering')

      if (Url.includes(btnName)) {
        btn.style['border'] = '1px solid rgb(81 151 242)'
        btn.value = true
        btnTitle.style['color'] = 'rgb(81 151 242)'
        btnTitle.style['font-weight'] = 'bold'
      } else { btn.value = false }


      filters.forEach((filter) => {
        const filterCheck = filter.querySelector('.filtering-check > img')
        const fName = filter.getAttribute('name')
        const fValue = filter.getAttribute('value')

        if (Url.includes(`${fName}=${fValue}`)) {
          filterCheck.src = '/static/image/check.png'
          filterCheck.alt = 'check'
        }

      })
      
      if (btn.value == false) {
        const filterCollapse = btn.querySelector('.filtering-collapse')
        const filterArrow = btn.querySelector('.filtering-img > img')

        filterCollapse.addEventListener('show.bs.collapse', () => {
          btn.style.border = '1px solid rgb(81 151 242)'
          filterArrow.style.transform = 'rotate(180deg)'
        })
        
        filterCollapse.addEventListener('hide.bs.collapse', () => {
          btn.style.border = '1px solid rgb(240 240 240)'
          filterArrow.style.transform = ''
        })

      }
    })

    // 배너 스타일 변환
    const banner = document.querySelector('.listing-banner')
    const bannerTitle = document.querySelector('.listing-banner-title')
    const bannerContent = document.querySelector('.listing-banner-content')
    const bannerImage = document.querySelector('.listing-banner-image > img')
    const Url = window.location.href

    if (Url.includes('category=traditional')) {

      banner.style['background-color'] = 'rgb(255, 251, 244)'
      bannerTitle.textContent = '전통주'
      bannerContent.textContent = '맛있는 막걸리는 여기 다 있어요.'
      bannerImage.src = '/static/image/전통주.png'
      bannerImage.alt = '전통주'

    } else if (Url.includes('category=beer')) {

      banner.style['background-color'] = 'rgb(242, 236, 255)'
      bannerTitle.textContent = '맥주'
      bannerContent.textContent = '시원한 맥주들이 모여있어요.'
      bannerImage.src = '/static/image/맥주.png'
      bannerImage.alt = '맥주'

    } else if (Url.includes('category=whiskey')) {

      banner.style['background-color'] = 'rgb(247, 250, 253)'
        bannerTitle.textContent = '위스키'
        bannerContent.textContent = '하루를 끝내기에 좋은 술이에요.'
        bannerImage.src = '/static/image/위스키.svg'
        bannerImage.alt = '위스키'

    } else if  (Url.includes('category=wine')) {

      banner.style['background-color'] = 'rgb(255, 242, 245)'
      bannerTitle.textContent = '와인'
      bannerContent.textContent = '분위기에는 와인이죠.'
      bannerImage.src = '/static/image/와인.svg'
      bannerImage.alt = '와인'

    }


    // 필터링


    // 가격 외
    const buttons = document.querySelectorAll('.filtering')

    buttons.forEach((btn) => {

      const btnName = btn.getAttribute('name')
      const btnValue = btn.getAttribute('value')

      btn.addEventListener('click', () => {
        const Url = window.location.href

        if (Url.includes(`&${btnName}=${btnValue}`)) {

          const newUrl = Url.replace(`&${btnName}=${btnValue}`,'')
          window.location.href = newUrl

        } else {

          const newUrl = `${Url}&${btnName}=${btnValue}`
          window.location.href = newUrl
          
        }
        
      })
    })


    // 가격
    const prices = document.querySelectorAll('.pricing')

    prices.forEach((price) => {

      const priceName = price.getAttribute('name')
      const priceValue = price.getAttribute('value')

      price.addEventListener('click', () => {
        const Url = window.location.href   

        if (Url.includes(`&${priceName}=${priceValue}`)) {

          const newUrl = Url.replace(`&${priceName}=${priceValue}`,'')
          window.location.href = newUrl

        } else {

          // let reUrl = Url.replace('&price=0,10000','')
          // reUrl = reUrl.replace('&price=10000,30000','')
          // reUrl = reUrl.replace('&price=30000,50000','')
          // reUrl = reUrl.replace('&price=50000,100000','')
          // reUrl = reUrl.replace('&price=100000,1000000','')
      
          const reUrl = Url.replace(/&price=\d+,\d+/g,'')

          const newUrl = `${reUrl}&price=${priceValue}`
          window.location.href = newUrl

        }
      })
    })

    // 가격 검색
    const priceSubmit = document.querySelector('.price-search-submit')

    priceSubmit.addEventListener('click', (event) => {
      const num1 = document.querySelector('.price-number1').value
      const num2 = document.querySelector('.price-number2').value

      const Url = window.location.href
      const reUrl = Url.replace(/&price=\d+,\d+/g,'')
      const newUrl = `${reUrl}&price=${num1},${num2}`

      window.location.href = newUrl
    })

  ```

<br/>

## views.py
- ```python
    def listing(request):
    # products = get_list_or_404(Product)
    category = request.GET.get('category','')

    alcohol_percentage = request.GET.getlist('dosu','')
    a1,a2 = 100,0
    if alcohol_percentage:
        for alcohol_per in alcohol_percentage:
            a1 = min(a1,int(alcohol_per.split(',')[0]))
            a2 = max(a2,int(alcohol_per.split(',')[1]))
    else: a1,a2 = 0,100

    sweetness = request.GET.getlist('sweet',['low','middle','strong'])
    sourness = request.GET.getlist('sourness',['low','middle','strong'])
    bitterness = request.GET.getlist('bitterness',['low','middle','strong'])
    carbonated = request.GET.getlist('carbonated',['True','False'])

    price = request.GET.get('price','')
    if price: p1,p2 = price.split(',')
    else: p1,p2 = 0,1000000

    if category == 'all':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category = category)

    products = products.filter(
        alcohol_percentage__gte=int(a1),
        alcohol_percentage__lte=int(a2),
        sweetness__in=sweetness,
        sourness__in=sourness,
        bitterness__in=bitterness,
        carbonated__in=carbonated,
        discounted_price__gte=int(p1),
        discounted_price__lte=int(p2)
    )

    context = {
        'products': products,
        'cate': category,
    }
    return render(request, 'products/listing.html', context)
  ```