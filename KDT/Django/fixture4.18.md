# Django - Fixtures

<br/>

## 개요
- fixtures
  - Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
  - Django가 직접 만들기 때문에 데이터베이스 구조에 맞춰 작성되어있음
- 초기 데이터의 필요성
  - 협업하는 A,B 유저가 있음
    - A가 먼저 프로젝트 작업 후 github에 push
      - gitignore설정으로 인해 DB는 업로드하지 않기 때문에 A가 작성한 데이터는 올라가지 않음
    - B가 github에서 A가 push한 프로젝트를 pull or clone함
      - 마찬가지로 프로젝트는 받았지만 A가 생성하고 조작한 DB가 없는 프로젝트를 받게 됨
  - 이처럼 Django 프로젝트의 앱을 처음 설정할 때 동일하게 준비 된 데이터로 데이터베이스를 미리 채우는 것이 필요한 순간이 존재
  - Django에서는 fixtures를 사용해 앱에 `초기 데이터(initial data)`를 제공 가능

<br/>

## 초기 데이터 제공하기
- 사전 준비
  - M:N까지 모두 작성된 Django 프로젝트에서 유저, 게시글, 댓글, 좋아요 등 각 데이터를 최소 2개 이상 생성해두기
- fixtures 명령어
  - dumpdata
    - 생성(데이터 추출)
    - 데이터베이스의 모든 데이터를 출력, 여러 모델을 하나의 json 파일로 만들 수 있음
    - `$ python manage.py dumpdata [app_name[.ModelName] [app_name[.ModelName]] ...] filename.json`
    - ex / `$ python manage.py dumpdata articles.article > articles.json`
  - loaddata
    - 로드(데이터 입력)
    - fixtures 데이터를 데이터베이스로 불러오기

<br/>

### dumpdata
  - fixtures 생성
    - `$ python manage.py dumpdata --indent 4 articles.user > users.json`
    - `$ python manage.py dumpdata --indent 4 articles.article > articles.json`
    - `$ python manage.py dumpdata --indent 4 articles.comment > comments.json`

<br/>

### loaddata
  - fixtures 기본 경로
    - `app_name/fixtures/`
    - Django는 설치된 모든 app의 디렉토리에서 fixtures폴더 이후의 경로로 fixtures파일을 찾아 load함
    - `articles/fixtures/articles.json, users.json, comments.json` 이동
    - articles로 옮기는 이유는 dumpdata에서 articles의 경로로 설정했기 때문
  - fixtures 불러오기
    - `$ python manage.py loaddata users.json articles.json comments.json`
    - 나열 순서 중요!
  - 순서 주의사항
    - loaddata를 한 번에 실행하지 않고 하나씩 실행한다면 모델 관계에 따라 순서가 중요할 수 있음
      - comment는 article에 대한 key 및 user에 대한 key가 필요
      - article은 user에 대한 key가 필요
    - 즉, 현재 모델 관계에서는 user -> article -> comment 순으로 data를 넣어야 오류가 발생하지 않음
      - `$ python manage.py loaddata users.json`
      - `$ python manage.py loaddata articles.json`
      - `$ python manage.py loaddata comments.json`

<br/>

## 참고
- 모든 모델을 한번에 dump하기 / 권장 x
  - 3개의 모델을 하나의 json파일로
    - `$ python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json`
  - 모든 모델을 하나의 json파일로
    - `$ python manage.py dumpdata --indent 4 > data.json`
- fixtures는 직접 만드는 것이 아님
  - 반드시 dumpdata를 사용하여 생성하는 것
- loaddata 시 encoding codec관련 에러가 발생하는 경우
  - dumpdata시 추가 옵션 작성
    - `$ python -Xutf8 manage.py dumpdata ...`
  - 메모장 활용
    - 메모장으로 json파일 열기
    - 다른 이름으로 저장
    - 인코딩을 UTF8로 선택 후 저장

<br/>

### 정리
- dumpdata
  - `$ python -Xutf8 manage.py dumpdata --indent 4 articles.user > users.json`
  - `$ python -Xutf8 manage.py dumpdata --indent 4 articles.article > articles.json`
  - `$ python -Xutf8 manage.py dumpdata --indent 4 articles.comment > comments.json`
- fixtures 기본 경로
    - `app_name/fixtures/`
- 파일 경로 이동 / dumpdata에서 작성한 앱 이름 기준
    - `articles/fixtures/articles.json, users.json, comments.json`
- 순서 유의해서 loaddata
  - `$ python manage.py loaddata users.json articles.json comments.json`

<br/>

### 한 번에 넣기
- dumpdata
  - `$ python -Xutf8 manage.py dumpdata > xxx.json`
- loaddata
  - `$ python manage.py loaddata xxx.json`
