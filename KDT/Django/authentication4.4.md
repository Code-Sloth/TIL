# Django - Cookie & Session

<br/>

## HTTP
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약
- 웹(WWW)에서 이루어지는 `모든 데이터 교환`의 기초
- 비 연결 지향(connectionless)
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
- 무상태(stateless)
  - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 `상태 정보`가 유지되지 않음
  - 문제 : ex / 장바구니에 담은 상품을 유지 못하거나 로그인 상태를 유지할 수 없음

<br/>

## 쿠키
- 서버가 사용자의 웹 브라우저에 전송하는 작은 `데이터 조각`
- 클라이언트 측에서 저장되는 작은 데이터 파일이며, 사용자 인증, 사용자 추적, 상태 유지 등에서 사용되는 `데이터 저장 방식`
- ex / 매 요청마다 로그인 정보를 보냄

<br/>

### 쿠키 사용 예시
- `브라우저(클라이언트)`는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
- 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
  - 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 `기억` 시켜 주기 때문
- ex / 쿠팡
  - 개발자 도구 - Network 탭 - cartView.pang 확인
  - 서버는 응답과 함께 `Set-Cookie` 응답 헤더를 브라우저에게 전송
    - 이 헤더는 클라이언트에게 쿠키를 저장하라고 전달하는 것
  - Application 탭 - Coockies
  - 마우스 우측 버튼 - Clear 후 새로고침
  - 빈 장바구니로 변경된 것을 확인

<br/>

### 쿠키 사용 목적
- 세션 관리 (Session management)
  - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리
- 개인화 (Personalization)
  - 사용자 선호, 테마 등의 설정
- 트래킹 (Tracking)
  - 사용자 행동을 기록 및 분석

<br/>

### 세션(Session)
- `서버` 측에서 생성되어 클라이언트와 서버 간의 상태를 유지
- 상태 정보를 저장하는 데이터 저장 방식
- 쿠키에 세션 데이터를 저장하여 매 요청시마다 `세션 데이터`를 함께 보냄
- 작동 예시
  - 클라이언트가 로그인을 하면 서버가 session 데이터를 생성 후 저장
  - 생성된 session 데이터에 인증 할 수 있는 session id를 발급
  - 발급한 session id를 클라이언트에게 응답
  - 클라이언트는 응답 받은 session id를 쿠키에 저장
  - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
  - 쿠키는 요청 때마다 서버와 함께 전송 되므로 서버에서 `session id`를 확인해 로그인 되어있다는 것을 알도록 함

<br/>

### 쿠키 및 세션 활용 로그인 프로세스
- 사용자가 로그인하면 웹 사이트 서버는 해당 사용자에 대한 세션을 생성하고 서버 측에 세션 ID를 저장
- 서버는 또한 세션 ID를 포함하는 쿠키를 사용자의 웹 브라우저로 보냄
- 후속 요청에서 사용자의 웹 브라우저는 쿠키를 다시 서버로 전송하여 서버가 세션 ID를 검색하고 사용자가 여전히 인증되었는지 확인할 수 있도록 함
- 사용자가 로그아웃하거나 세션이 만료되면 서버는 세션을 삭제하고 쿠키를 무효화하여 사용자가 보호된 리소스에 엑세스하지 못하도록 함

<br/>

## 참고
- 쿠키 종류별 Lifetime
  - Session cookie
    - 현재 세션이 종료되면 삭제됨
    - 브라우저 종료와 함께 세션이 삭제됨
  - Persistent cookies
    - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨
- 세션 in Django
  - Django는 `database-backed sessions 저장 방식`을 기본 값으로 사용
  - session 정보는 DB의 django_session테이블에 저장
  - Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄
  - Django는 우리가 `session 메커니즘(복잡한 동작원리)`에 대부분을 생각하지 않게끔 많은 도움을 줌

<br/>

# Django 인증 시스템

<br/>

## Django Authentication System
- `사용자 인증`과 관련된 기능을 모아 놓은 시스템
- 인증과 권한 부여를 함께 제공 및 처리
- ```python
    # settings.py

    INSTALLED_APPS = [
        'articles',
        'django_extensions',
        'django.contrib.admin',
        'django.contrib.auth', # <==
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
  ```
- Authentication(인증) : 사용자가 누구인지 확인하는 것
- Authorization(권한) : 인증된 사용자가 수행할 수 있는 작업을 결정
- 사전 설정
  - app accounts 생성 및 등록
  - app_name = 'accounts'

<br/>

## Custom User model
- django가 기본적으로 제공하는 `User model`은 내장된 auth모듈의 User클래스를 사용
- 별도의 설정 없이 사용할 수 있어 간편하지만, `직접 수정할 수 없는` 문제
- 대체하기
    - AbstractUser를 상속받는 커스텀 User클래스 작성
    - 기존 User클래스도 AbstractUser를 상속받기 때문에 커스텀 User클래스도 완전히 `같은 모습`을 가지게 됨
    - ```python
        # accounts/models.py

        from django.contrib.auth.models import AbstractUser

        class User(AbstractUser):
          pass
      ```
    - django프로젝트가 사용하는 기본 User모델을 우리가 작성한 User모델로 지정(수정 전 'auth.User')
    - ```python
        # settings.py

        AUTH_USER_MODEL = 'accounts.User'
      ```
    - 기본 User모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음
    - ```python
        # accounts/admin.py

        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin
        from .models import User

        admin.site.register(User, UserAdmin)
      ```
- `주의` : 프로젝트 중간에 AUTH_USER_MODEL을 변경할 수 없음
- User모델을 대체해야 하는 이유
  - Django는 새 프로젝트를 시작하는 경우 비록 기본 User모델이 충분하더라도 커스텀 User모델을 설정하는 것은 `강력하게 권장`
  - 커스텀 User모델은 기본 User모델과 동일하게 작동하면서도 필요한 경우 나중에 `맞춤 설정`할 수 있기 때문
  - 단, User모델 대체 작업은 프로젝트의 모든 migrations혹은 첫 migrate를 `실행하기 전에` 이 작업을 마쳐야 함

<br/>

## Login
- Session을 Create하는 과정
- AuthenticationForm()
  - 로그인을 위한 built-in form
- 로그인 로직 작성
    - ```python
        # accounts/urls.py

        from django.urls import path
        from . import views

        app_name = 'accounts'
        urlpatterns = [
            path('login/', views.login, name='login'),
            
        ]
      ```
    - ```html
        <!-- accounts/login.html -->

        <h1>로그인</h1>
        <form action="{% url 'accounts:login' %}" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit">
        </form>
      ```
    - ```python
        # accounts/views.py

        from django.shortcuts import render, redirect
        from django.contrib.auth.forms import AuthenticationForm
        from django.contrib.auth import login as auth_login

        # Create your views here.

        def login(request):
            if request.method == 'POST':
                form = AuthenticationForm(request, request.POST)
                if form.is_valid():
                    auth_login(request, form.get_user())
                    return redirect('articles:index')
            else:
                form = AuthenticationForm()

            return render(request, 'accounts/login.html', {'form' : form})
      ```
- login(request, user)
  - 인증된 사용자를 로그인 하는 함수
- get_user()
  - AuthenticationForm의 인스턴스 메서드
  - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

<br/>

## Logout
- Session을 Delete하는 과정
- logout(request)
  - 현재 요청에 대한 `session data`를 DB에서 삭제
  - 클라이언트의 쿠키에서도 `sessionid`를 삭제
- 로그아웃 로직 작성
    - ```python
        # accounts/urls.py

        from django.urls import path
        from . import views

        app_name = 'accounts'
        urlpatterns = [
            path('login/', views.login, name='login'),
            path('logout/', views.logout, name='logout')
        ]
      ```
    - ```html
        <!-- articles/index.html -->

        <h1>Articles</h1>
        <a href="{% url 'accounts:login' %}">Login</a>
        <form action="" method="POST">
          {% csrf_token %}
          <input type="submit" value='Logout'>
        </form>
      ```
    - ```python
        # accounts/views.py

        from django.shortcuts import render, redirect
        from django.contrib.auth.forms import AuthenticationForm
        from django.contrib.auth import login as auth_login
        from django.contrib.auth import logout as auth_logout

        def logout(request):
          auth_logout(request)
          return redirect('articles:index')
      ```

<br/>

## Template with Authentication data
- 템플릿에서 인증 관련 데이터를 출력하는 방법
    - ```html
        <!-- articles/index.html -->

        <h3>Hello, {{ user }}</h3>
        <!-- 화면에서는 비로그인 시, AnonymousUser로 출력 -->
        <!-- 로그인 시, 내 id를 출력 -->
      ```
    - context processors
      - 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
      - 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨
      - 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해 둔 것
      - ```python
          # settings.py

          TEMPLATES = [
              {
                  'BACKEND': 'django.template.backends.django.DjangoTemplates',
                  'DIRS': [],
                  'APP_DIRS': True,
                  'OPTIONS': {
                      'context_processors': [
                          'django.template.context_processors.debug',
                          'django.template.context_processors.request',
                          'django.contrib.auth.context_processors.auth',
                          'django.contrib.messages.context_processors.messages',
                      ],
                  },
              },
          ]
        ```

<br/>

## 참고
- User 모델 상속 관계
  - models.Model => class AbstractBaseUser => class AbstractUser => class User
  - AbstractUser class
    - 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 `추상 기본 클래스`
    - Abstract base classes(추상 기본 클래스)
      - 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
      - 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨
      - https://docs.python.ort/3/library/abc.html
- 유저 모델 대체하기 Tip
  - 대체하는 과정을 외우기 어려울 경우 해당 공식문서를 보며 `순서대로 진행`하는 것을 권장
  - https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model
