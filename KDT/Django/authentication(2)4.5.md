# Authentication 2

<br/>

## 회원가입
- User객체를 `Create`하는 것
- UserCreationForm()
  - 회원가입을 위한 built-in `ModelForm`
  - https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L75
- 회원가입 페이지 작성
    - ```python
        # accounts/urls.py

        from django.urls import path
        from . import views

        app_name = 'accounts'
        urlpatterns = [
            ...,
            path('signup/', views.signup, name='signup'),
        ]
      ```
    - ```html
        <!-- accounts/signup.html -->

        <h1>회원 가입</h1>
        <form action="{% url 'accounts:signup' %}" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit">
        </form>
      ```
    - ```python
        # accounts/views.py

        def signup(request):
          if request.method == 'POST':
              form = UserCreationForm(request.POST)
              if form.is_valid():
                  form.save()
                  return redirect('articles:index')
          else:
              form = UserCreationForm()
          context = {
              'form': form
          }
          return render(request, 'accounts/signup.html', context)
      ```
- 회원가입 진행 후 `에러` 페이지 확인
  - 회원가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이기 때문
  - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L106
  - 커스텀 유저 모델을 사용하려면 다시 작성해야 하는 forms
    - UserCreationForm / UserChangeForm
      - 두 form 모두 class Meta: model=User가 등록된 form이기 때문
- 커스텀 Form 작성
  - ```python
      # accounts/forms.py

      from django.contrib.auth.forms import UserCreationForm, UserChangeForm
      # django User 객체에 대한 직접 참조를 권장하지 않음
      # from .models import User

      # 대신 다음과 같은 함수를 제공
      # get_user_model은 현재 프로젝트에 활성화 되어있는 User객체를 반환해줌
      from django.contrib.auth import get_user_model

      class CustomUserCreationForm(UserCreationForm):
          class Meta(UserCreationForm.Meta):
              # 현재 우리가 사용하는 User class로 재정의
              model = get_user_model()

      class CustomUserChangeForm(UserChangeForm):
          class Meta(UserChangeForm.Meta):
              model = get_user_model()
    ```
- 회원가입 로직 수정
  - ```python
      # accounts/views.py

      from .forms import CustomUserCreationForm

      def signup(request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)
    ```

<br/>

### User 모델을 직접 참조하지 않는 이유
- User 모델을 `get_user_model()`를 사용해 참조하면 커스텀 User모델을 자동으로 반환해주기 때문
- Django는 User클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 강조

<br/>

## 회원 탈퇴
- User객체를 `Delete`하는 것
- 회원탈퇴 로직 작성
    - ```python
        # accounts/urls.py

        from django.urls import path
        from . import views

        app_name = 'accounts'
        urlpatterns = [
            ...,
            path('delete/', views.delete, name='delete'),
        ]
      ```
    - ```html
        <!-- accounts/index.html -->

        <form action="{% url 'accounts:delete' %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="Delete">
        </form>
      ```
    - ```python
        # accounts/views.py

        def delete(request):
          request.user.delete()
          return redirect('articles:index')
      ```

<br/>

## 회원정보 수정
- User객체를 `Update`하는 것
- UserChangeForm()
  - 회원가입을 위한 built-in ModelForm
  - https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L135
- 회원정보 수정 페이지 작성
    - ```python
        # accounts/urls.py

        from django.urls import path
        from . import views

        app_name = 'accounts'
        urlpatterns = [
            ...,
            path('update/', views.update, name='update'),
        ]
      ```
    - ```html
        <!-- accounts/update.html -->

        <h1>회원정보 수정</h1>
        <form action="{% url 'accounts:update' %}" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit">
        </form>
      ```
    - ```python
        # accounts/views.py

        def update(request):
          if request.method == 'POST':
              form = CustomUserChangeForm(request.POST, instance=request.user)
              if form.is_valid():
                  form.save()
                  return redirect('articles:index')
          else:
              form = CustomUserChangeForm(instance=request.user)
          context = {
              'form': form
          }
          return render(request, 'accounts/update.html', context)
      ```
- UserChangeForm 사용 문제점
  - 일반 사용자가 접근해서는 안 될 정보들(fields)까지 모두 수정이 가능해짐
  - admin 인터페이스에서 사용되는 ModelForm이기 때문
  - 따라서 CustomUserChangeForm에서 접근 가능한 필드를 조정
  - https://github.com/django/django/blob/main/django/contrib/auth/models.py#L334
  - ```python
      # accounts/forms.py

      class CustomUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.Meta):
            model = get_user_model()
            fields = ('email','first_name','last_name',)
    ```

<br/>

## 비밀번호 변경
- django는 비밀번호 변경 페이지를 회원정보 수정 form에서 별도 주소로 안내
- PasswordChangeForm()
  - 비밀번호 변경을 위한 built-in Form
  - https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L360
- 비밀번호 변경 페이지 작성
    - ```python
        # accounts/urls.py

        from django.urls import path
        from . import views

        app_name = 'accounts'
        urlpatterns = [
            ...,
            path('password/', views.change_password,  name='change_password'),
        ]
      ```
    - ```html
        <!-- accounts/change_password.html -->

        <h1>비밀번호 변경</h1>
        <form action="{% url 'accounts:change_password' %}" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit">
        </form>
      ```
    - ```python
        # accounts/views.py

        from django.contrib.auth.forms import PasswordChangeForm

        def change_password(request):
          if request.method == 'POST':
              form = PasswordChangeForm(request.user, request.POST)
              if form.is_valid():
                  form.save()
                  return redirect('articles:index')
          else:
              form = PasswordChangeForm(request.user)
          context = {
              'form': form
          }
          return render(request, 'accounts/change_password.html', context)
      ```
- PasswordChangeForm 인자 순서
    - ```python
        def __init__(self, user, *args, **kwargs):
          self.user = user
          super().__init__(*args, **kwargs)
      ```
    - https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L316
- 암호 변경 시 `세션 무효화`
  - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어버려 로그인 상태가 유지되지 못함
  - 비밀번호는 잘 변경되었으나 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문
  - 따라서 기존 세션은 필요없어져 세션을 삭제시킴
  - 유지하기 위한 함수를 사용 가능
  - update_session_auth_hash(request, user)
  - https://docs.djangoproject.com/en/3.2/topics/auth/default/#django.contrib.auth.update_session_auth_hash
    - ```python
        # accounts/views.py

        from django.contrib.auth import update_session_auth_hash

        def change_password(request):
          if request.method == 'POST':
              form = PasswordChangeForm(request.user, request.POST)
              if form.is_valid():
                  form.save()
                  # 비밀번호 변경시 세션 무효화 방지
                  update_session_auth_hash(request, request.user)
                  return redirect('articles:index')
          else:
              form = PasswordChangeForm(request.user)
          context = {
              'form': form
          }
          return render(request, 'accounts/change_password.html', context)
      ```

<br/>

## 로그인 사용자에 대한 접근 제한
- is_authenticated (속성)
  - 사용자가 인증되었는지 여부를 알 수 있는 User model의 속성(attributes)
  - 모든 User 인스턴스에 대해 항상 `True`인 읽기 전용 속성이며, AnonymousUser에 대해서는 항상 `False`임
  - 권한(permission)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않음
  - 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정
    - ```html
        <!-- articles/index.html -->

        {% if request.user.is_authenticated %}

          <h3>안녕하세요, {{ user }} 님!</h3>

          <form action="{% url 'accounts:logout' %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="Logout">
          </form>

          <form action="{% url 'accounts:delete' %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="회원탈퇴">
          </form>
        
          <a href="{% url 'accounts:update' %}">회원정보 수정</a>

        {% else %}

          <a href="{% url 'accounts:login' %}">Login</a>

          <a href="{% url 'accounts:signup' %}">Signup</a>

        {% endif %}
      ```
  - url로도 접근하지 못하게 설정
    - ```python
        # accounts/views.py 

        def login(request):
          if request.user.is_authenticated:
              return redirect('articles:index')

        def signup(request):
          if request.user.is_authenticated:
              return redirect('articles:index')
      ```
- login_required
  - 인증된 사용자에 대해서만 view함수를 실행시키는 데코레이터
  - 로그인하지 않은 사용자의 경우 `/accounts/login/`주소로 redirect시킴
  - 인증된 사용자만 게시글을 작성/수정/삭제 할 수 있도록 수정
    - ```python
        # articles/views.py

        from django.contrib.auth.decorators import login_required

        @login_required
        def create(request):
          pass

        @login_required
        def delete(request, article_pk):
          pass

        @login_required
        def update(request, article_pk):
          pass
      ```
  - 인증된 사용자만 게시글을 로그아웃/탈퇴/수정/비밀번호 변경 할 수 있도록 설정
    - ```python
        # accounts/views.py

        from django.contrib.auth.decorators import login_required

        @login_required
        def logout(request):
          pass

        @login_required
        def delete(request):
          pass

        @login_required
        def update(request):
          pass

        @login_required
        def change_password(request):
          pass
      ```

<br/>

## 참고
- 데코레이터(Decorator)
  - 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능만을 추가 해주는 함수
  - ```python
      def hello(func):
        def wrapper():
          print('hi')
          func()
          print('hi')
        return wrapper

      @hello
      def bye():
        print('bye')
      
      bye()

      # hi
      # bye
      # hi
    ```
- 회원가입 후 로그인까지 진행하려면
  - ```python
      # accounts/views.py

      def signup(request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save() # 변수에 저장
                auth_login(request, user) # 로그인
                return redirect('accounts:index')
        else:
            form = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'form':form})
    ```
- 탈퇴하면서 유저의 세션 정보도 함께 지우고 싶을 경우
    - ```python
        # accounts/views.py

        def delete(request):
          request.user.delete()
          auth_logout(request)
      ```
    - 먼저 로그아웃 해버리면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 유저 정보 또한 없어지므로 순서 중요
