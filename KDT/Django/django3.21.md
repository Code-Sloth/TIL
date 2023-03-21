# Django Design Pattern

<br/>

## django 프로젝트와 앱
- django project
  - 애플리에키션의 집합
  - DB 설정, URL 연결, 전체 앱 설정 등을 처리
- django application
  - 독립적으로 작동하는 기능 단위 모듈
  - 각자 특정한 기능을 담당하여 다른 앱들과 함께 하나의 프로젝트를 구성
  - MTV 패턴에 해당하는 파일 및 폴더를 담당
- 블로그
  - 프로젝트 : 블로그 전체 설정 담당
  - 앱 : 게시글, 댓글, 카테고리 회원 관리 등 (DB, 로직, 화면)
- 앱 생성
  - python manage.py startapp articles
  - articles 부분의 앱의 이름은 복수형을 권장
- 앱 등록 (생성 후 등록해야 함)
  - settings.py / INSTALLED_APPS / 'articles' 추가

<br/>

## django 디자인 패턴
- 디자인 패턴
  - 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책
  - 공통적인 문제를 해결하는데 쓰이는 형식화 된 관행
- MVC 디자인 패턴 (Model - View - Controller)
  - 애플리케이션을 구조화하는 대표적인 패턴
  - 데이터, 사용자 인터페이스, 비즈니스 로직을 분리
  - 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지보수할 수 있는 애플리케이션을 만들기 위해
- MTV 디자인 패턴 (Model - Template - View)
  - django에서 애플리케이션을 구조화하는 패턴
  - 기존 MVC 패턴과 동일하나 명칭을 다르게 정의

<br/>

### 프로젝트 구조
- settings.py
  - 프로젝트의 모든 설정을 관리
- urls.py
  - URL과 이에 해당하는 적절한 views를 연결
- ___init___.py
  - 해당 폴더를 패키지로 인식하도록 설정
- asgi.py
  - 비동기식 웹 서버와의 연결 관련 설정
- wsgi.py
  - 웹 서버와의 연결 관련 설정
- manage.py
  - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

<br/>

### 앱 구조
- admin.py
  - 관리자용 페이지 설정
- models.py
  - DB와 관련된 Model을 정의
  - MTV 패턴의 M
- views.py
  - HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환
  - MTV 패턴의 V
- apps.py
  - 앱의 정보가 작성된 곳
- tests.py
  - 프로젝트 테스트 코드를 작성하는 곳
