# 장고 가이드 (Django Guide)

<br/>

## 사전 준비
- VSCode extension
  - `Django` 설치
  - `SQLite Viewer` 설치
- django extension 관련 설정
  - Help => Show All Commands => JSON 검색 => Preference: Open User Settings (JSON) 선택
  - ```python
      {
        ... 생략 ...,

        // Django
        "files.associations": {
          "**/*.html": "html",
            "**/templates/**/*.html": "django-html",
          "**/templates/**/*": "django-txt",
          "**/requirements{/**,*}.{txt,in}": "pip-requirements"
        },
        "emmet.includeLanguages": {
          "django-html": "html"
        }
      }
      # 입력
    ```
    
<br/>

## Django 프로젝트 및 가상환경
1. 가상환경 생성
    - `python -m venv venv`
2. 가상환경 활성화
    - `source venv/Scripts/activate`
    - vscode에서 ctrl + shift + p / interpreter 검색 후 활성화 => 터미널 창
3. django 설치
    - `pip install django==3.2.18`
4. 의존성 파일 생성(패키지 설치시마다 진행)
    - `pip freeze > requirements.txt`

5. .gitignore 파일 생성 후 입력
    - .gitignore
    - add하기 전에 설정해야 함
    - https://www.toptal.com/developers/gitignore/
    - visualstudiocode, windows, macos, django
6. git 저장소 생성
    - `git init`


7. django 프로젝트 생성
    - `django-admin startproject firstpjt .`
8. django 서버 실행
    - `python manage.py runserver`
9. `http://127.0.0.1:8000/` 접속 후 확인

<br/>

### Django 프로젝트 및 가상환경 받는 사람
1. `pull`
2. `python -m venv venv`
3. `pip list`
4. `pip install -r requirements.txt`

<br/>

## Django
1. `python manage.py startapp articles`
2. `firstpjt / settings.py / # Application definition`
      - ```python
          INSTALLED_APPS = [
            # 앱 등록 권장 순서
            # 1. local app
            'articles', # 추가 입력

            # 2. 3rd party app (설치를 통해 추가하는 앱)

            # 3. 기본 django app
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]
        ```

3. `firstpjt / urls.py`
    - ```python
        from django.contrib import admin
        from django.urls import path
        # urls.py 입장에서는 
        # articles라는 패키지에서
        # views라는 모듈을 가져오는 것
        from articles import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('articles/', views.index),
            # https://128.0.0.1:8000/articles/ 로 요청이 왔을 때
            # articles/views 파일의 index 함수를 호출
        ]
      ```

4. `articles / view.py`
    - ```python
        from django.shortcuts import render

        # Create your views here.
        # 특정 기능을 수행하는 view 함수들을 작성
        # 모든 view 함수는 첫번째 인자로 요청 객체를 필수적으로 받는다.
        def index(request):
            return render(request, 'articles/index.html')
        # articles/templates/articles/index.html 과 request 객체를 결합해
        # 응답 객체를 반환하는 index 뷰 함수 정의
      ```

5. `templates`
    - articles / templates 폴더 생성 / articles 폴더 생성 / index.html 파일 생성 및 작성

6. `페이지 확인`
    - https://127.0.0.1.8000/articles/
