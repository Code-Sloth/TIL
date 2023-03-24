# Django Model

<br/>

## Model
- SQLite
  - 오픈소스 RDBMS 중 하나로 django의 기본 DB로 사용됨 (DB가 파일로 존재하며 가볍고 호환성이 좋음)
- django model
  - DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
  - 테이블 구조를 설계하는 '청사진(blueprint)'

<br/>

### model 클래스
- ```python
    # articles/models.py

    class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
    # id필드는 자동 생성
  ```
- |id|title|content|
  |--|--|--|
  |..|..|..|
  |..|..|..|
  - 이런 테이블을 만들기 위한 설계도 / 모델 클래스 == 테이블 스키마
- model.Model
  - django.db.models 모듈의 Model이라는 부모 클래스를 상속 받아 작성
  - model 기능에 관련된 모든 설정이 담긴 클래스
    - https://github.com/django/django/blob/main/django/db/models/base.py#L459
  - 개발자는 테이블 구조를 어떻게 설계할 지에 대한 코드만 작성하도록 하기 위함
- title / content
  - 클래스 변수명 => 테이블의 각 필드 이름
- model Field 메서드
  - 테이블 필드의 데이터 타입
  - CharField() : 길이 제한 / TextField() : 길이 제한 x
  - https://docs.djangoproject.com/en/3.2/ref/models/fields/
- max_length=10
  - model Field 메서드의 키워드 인자
  - 테이블 필드의 제약조건 관련 설정

<br/>

## Migrations
- model 클래스의 변경사항(필드 생성, 추가 수정 등)을 DB에 최종 반영하는 방법

<br/>

### Migrations 실행
- `$ python manage.py makemigrations`
  - model class 기반으로 설계도(migration) 작성
- `$ python manage.py migrate`
  - 만들어진 설계도를 DB에 전달하여 반영
- 순서 (중간 단계 필수)
  - model class ==(makemigrations)>> migration 파일(설계도) ==(migrate)>> db.sqlite3
- migrate 후 DB 내에 생성 된 테이블 확인

<br/>

### Migrations 테이블 필드 추가
- ```python
    # articles/models.py

    class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```
- `$ python manage.py makemigrations`
  - 추가 입력 1
    - 이미 기존 테이블이 존재하기 때문에 필드를 추가 할 때 필드의 기본 값 설정이 필요
    - 1번은 직접 기본 값을 입력하는 방법
    - 2번은 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법
  - 추가 입력 2
    - 추가하는 필드의 기본 값을 입력해야 하는 상황
    - 날짜 데이터이기 때문에 직접 입력하기보다 django가 제안하는 기본 값을 사용 권장
    - 아무것도 입력하지 않고 enter를 누르면 django가 제안하는 기본 값으로 설정 됨 (timezone.now)
    - CharField 같은 경우 ''을 입력해주거나, (max_length=10, black=True)로 설정
- 002 파일이 생성된 후 `$ python manage.py migrate`
- 새로운 파일이 생성 되는 이유
  - model class에 변경사항이 생겼다면, 반드시 새로운 설계도를 생성하고 이를 DB에 반영해야 함

<br/>

### 테이블 Field
- CharField()
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - 필드의 최대 길이를 결정하는 max_length는 필수 인자
- TextField()
  - 글자의 수가 많을 때 사용
- DateTimeField()
  - 날짜와 시간을 넣을 때 사용
  - auto_now / updated_at에서 사용
    - 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장
  - auto_now_add / create_at에서 사용
    - 데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장

<br/>

## Admin site
- Automatic admin interface
  - django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
  - 데이터 관련 테스트 및 확인을 하기에 매우 유용
- admin 계정 생성
  - `$ python manage.py createsuperuser`
    - id 입력
    - email은 선택사항이기 때문에 입력x
    - 비밀번호 생성 시 보안상 터미널에 출력되지 않으니 무시하고 입력
- admin에 모델 클래스 등록
  - ```python
      # articles/admin.py

      from django.contrib import admin
      from .models import Article

      # admin site에 등록(register)하겠다.
      admin.site.register(Article)
    ```
- 로그인 후 등록된 모델 클래스 확인
- 데이터 CRUD 테스트 후 실제 테이블에 저장여부 확인
- http://127.0.0.1:8000/admin/

<br/>

## 참고
- Migrations 기타 명령어
  - `$ python manage.py showmigrations`
    - migrations 파일들이 migrate됐는지 여부를 확인하는 용도
    - X표시가 있으면 migrate가 완료되었음을 의미
  - `$ python manage.py sqlmigrate articles 0001`
    - 해당 migrations 파일이 SQL문으로 어떻게 해석되어 DB에 전달되는지 확인하는 용도
- 첫 migrate 시, 출력 내용이 많은 이유
  - 기본적으로 Django 프로젝트가 동작하기 위해 작성되어있는 기본 내장 app들에 대한 migration 파일들이 함께 migrate되기 때문
- 저장되는 현재 시간은 UTC 기준
- settings.py에서 language를 ko-kr로 변경 가능
- 초기화
  - 000n 파일들 삭제, venv/db.sqlite3 삭제 후 실행