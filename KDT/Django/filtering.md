# 필터링 구현

<br/>

## Url,JS를 이용한 필터링
- ```html
    <button class='filtering' name='dosu' value='low'>0%~10%</button>
    <button class='filtering' name='dosu' value='middel'>10%~20%</button>
    <button class='filtering' name='dosu' value='high'>20%~30%</button>
    <button class='filtering' name='dosu' value='very_high'>30%이상</button>

    <button class='filtering' name='sweet' value='low'>약한</button>
    <button class='filtering' name='sweet' value='middle'>중간</button>
    <button class='filtering' name='sweet' value='strong'>강한</button>

    <button class='filtering' name='sourness' value='low'>약한</button>
    <button class='filtering' name='sourness' value='middle'>중간</button>
    <button class='filtering' name='sourness' value='strong'>강한</button>

    <button class='filtering' name='bitterness' value='low'>약한</button>
    <button class='filtering' name='bitterness' value='middle'>중간</button>
    <button class='filtering' name='bitterness' value='strong'>강한</button>

    <button class='filtering' name='carbonated' value='True'>있음</button>
    <button class='filtering' name='carbonated' value='False'>없음</button>

    <button class='pricing' name='price' value='0,10000'>~1만원</button>
    <button class='pricing' name='price' value='10000,30000'>1만원~3만원</button>
    <button class='pricing' name='price' value='30000,50000'>3만원~5만원</button>
    <button class='pricing' name='price' value='50000,100000'>5만원~10만원</button>
    <button class='pricing' name='price' value='100000,1000000'>10만원 이상</button>

    <script>
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

      const prices = document.querySelectorAll('.pricing')

      prices.forEach((price) => {

        const priceName = price.getAttribute('name')
        const priceValue = price.getAttribute('value')

        price.addEventListener('click', () => {
          const Url = window.location.href   

          let reUrl = Url.replace('&price=0,10000','')
          reUrl = reUrl.replace('&price=10000,30000','')
          reUrl = reUrl.replace('&price=30000,50000','')
          reUrl = reUrl.replace('&price=50000,100000','')
          reUrl = reUrl.replace('&price=100000,1000000','')

          const newUrl = `${reUrl}&price=${priceValue}`
          window.location.href = newUrl
          
        })
      })
    </script>
  ```
- ```python
    def listing(request):
        # products = get_list_or_404(Product)
        category = request.GET.get('category','')
        alcohol_percentage = request.GET.get('dosu','')
        if alcohol_percentage: a1,a2 = alcohol_percentage.split(',')
        else: a1,a2 = 0,100
        sweetness = request.GET.get('sweet','')
        sourness = request.GET.get('sourness','')
        bitterness = request.GET.get('bitterness','')
        carbonated = request.GET.get('carbonated','')
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
            sweetness__icontains=sweetness,
            sourness__icontains=sourness,
            bitterness__icontains=bitterness,
            carbonated__icontains=carbonated,
            discounted_price__gte=int(p1),
            discounted_price__lte=int(p2)
        )

        context = {
            'products': products,
            'category': category,
        }
        return render(request, 'products/listing.html', context)
  ```