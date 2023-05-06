# 카카오 API

</br>

### kakao 사전 준비
- https://developers.kakao.com/docs/latest/ko/kakaopay/common
- API 생성
- IP 등록

<br/>

### settings.py
- ```python
    import os

    KAKAO_KEY = os.getenv('KAKAO_KEY')
  ```

<br/>

### urls.py
- ```python
    from django.urls import path
    from . import views

    app_name = 'products'
    urlpatterns = [
      ...,
      path('<int:product_pk>/kakaopay/', views.kakaopay, name='kakaopay'),
      path('<int:product_pk>/pay_success/', views.pay_success, name='pay_success'),
      path('pay_fail/', views.pay_fail, name='pay_fail'),
      path('pay_cancel/', views.pay_cancel, name='pay_cancel'),
    ]
  ```

<br/>

### views.py
- ```python
    import os
    KAKAO_KEY = os.getenv('KAKAO_KEY')

    @login_required
    def kakaopay(request, product_pk):
        kakao_price = request.POST.get('kakao-price')
        kakao_count = request.POST.get('kakao-count')
        product = Product.objects.get(pk=product_pk)
        
        admin_key = KAKAO_KEY
        url = f'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            'Authorization': f'KakaoAK {admin_key}',
        }
        data = {
            'cid': 'TC0ONETIME',
            'partner_order_id': product.pk, #주문 번호
            'partner_user_id': request.user.username, #유저 이름
            'item_name': product.title, #제품명
            'quantity': kakao_count, #수량
            'total_amount': kakao_price, #가격
            'tax_free_amount':'0',
    
            'approval_url':f'https://drinkit.kro.kr/products/{product.pk}/pay_success/', 
            'fail_url':'https://drinkit.kro.kr/products/pay_fail',
            'cancel_url':'https://drinkit.kro.kr/products/pay_cancel'
        }
        res = requests.post(url, data=data, headers=headers)
        result = res.json()
        request.session['tid'] = result['tid']
        return redirect(result['next_redirect_pc_url'])

    @login_required
    def pay_success(request, product_pk):
        product = Product.objects.get(pk=product_pk)
        url = 'https://kapi.kakao.com/v1/payment/approve'
        admin_key = KAKAO_KEY
        
        headers = {
            'Authorization': f'KakaoAK {admin_key}'
        }
        data = {
            'cid':'TC0ONETIME',
            'tid': request.session['tid'], #결제 고유 번호
            'partner_order_id': product.pk, #주문 번호
            'partner_user_id': request.user.username, #유저 아이디
            'pg_token': request.GET['pg_token'] 
        }
        res = requests.post(url, data=data, headers=headers)
        result = res.json()
        context = {
            'res':res,
            'result':result,
        }
        if result.get('msg'): #msg = 오류 코드
            return redirect('products:pay_fail')
        else:
            product.purchase_users.add(request.user, through_defaults={
                'title': product.title,
                'count': result['quantity'],
                'price': result['amount']['total']
            })
            return render(request, 'products/pay_success.html', context)

    @login_required
    def pay_fail(request):
        return render(request, 'products/pay_fail.html')

    @login_required
    def pay_cancel(request):
        return render(request, 'products/pay_cancel.html')
  ```

<br/>

### pay_success.html
- ```html
    {% extends 'base.html' %}
    {% load static %}
    {% block title %}결제완료{% endblock title %}

    {% block content %}
    <link rel="stylesheet" type="text/css" href="{% static 'css/kakao.css' %}">

    <div class='container'>
      <div class='complete-title'>
        결제가 완료되었습니다!
      </div>

      <div class='complete-box'>
        <div class='complete-user'>
          주문자 정보
        </div>

        <div class='complete-flex'>
          <h5>주문번호</h5>
          <p>{{ result.partner_order_id }}</p>
        </div>

        <div class='complete-flex'>
          <h5>주문자명</h5>
          <p>{{ result.partner_user_id }}</p>
        </div>

        <div class='complete-flex'>
          <h5>상품명</h5>
          <p>{{ result.item_name }}</p>
        </div>

        <div class='complete-flex'>
          <h5>구매수량</h5>
          <p>{{ result.quantity }}</p>
        </div>

        <div class='complete-flex'>
          <h5>결제금액</h5>
          <p>{{ result.amount.total }}</p>
        </div>

        <div class='complete-flex'>
          <h5>결제승인시각</h5>
          <p>{{ result.approved_at }}</p>
        </div>

        <div class='kakao-main w-100 mt-5'>
          <a href="{% url 'products:index' %}">메인으로 이동</a>
        </div>
      </div>

    </div>

    {% endblock content %}
  ```

