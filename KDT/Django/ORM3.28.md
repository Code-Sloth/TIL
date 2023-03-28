# Django ORM

<br/>

## ORM (Object-Relational-Mapping)
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

<br/>

## QuerySet API
- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구
- API를 사용하여 SQL이 아닌 Python코드로 데이터를 처리
- `Article.objects.all()` / Model class.Manager.Queryset API

<br/>

### Query
- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- 쿼리문을 작성한다
  - 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.
- 이 때, 파이썬으로 작성한 코드가 `ORM`에 의해 `SQL`로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 `QuerySet`이라는 자료 형태로 변환하여 우리에게 전달

<br/>

### QuerySet
- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
- Django ORM을 통해 만들어진 자료형
- 단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

<br/>

## ORM CREATE
- 외부 라이브러리 설치 및 설정
  - `$ pip install ipython`
  - `$ pip install django-extensions`
  - INSTALLED_APPS에 'django_extensions' 추가 / 언더바 유의
  - `$ pip freeze > requirements.txt` 업데이트

<br/>

### Django shell
- django 환경 안에서 실행되는 python shell
  - 입력하는 QuerySet API 구문이 django 프로젝트에 영향을 미침
- 실행 : `$ python manage.py shell_plus`
- 데이터 객체를 생성하는 방법
  - ```python
      # 방법 1 / 특정 테이블에 새로운 행을 추가하여 데이터 추가

      article = Article()
      article.title = '제목1'
      article.content = '내용1'
      article.save()

      # 방법 2

      article = Article(title='제목2', content='내용2')
      article.save()

      # 방법 3

      Article.objects.create(title='제목3', content='내용3')
    ```

<br/>

## ORM READ
- 데이터 조회
  - get()
    - 객체를 찾을 수 없으면 `DoesNotExist` 예외 발생
    - 객체가 둘 이상이면 `MultipleObjectsReturned` 예외 발생
    - 따라서 primary key와 같이 `고유성`을 보장하는 조회에서 사용
  - ```python
      # 전체 데이터 조회
      Article.objects.all()

      # 단일 데이터 조회
      Article.objects.get(pk=1) # pk=1인 단일 데이터
      Article.objects.get(content='제목2') # content가 제목2인 단일 데이터
      
      # 여러 데이터 조회
      Article.objects.filter(title='제목3') # title이 제목3인 모든 데이터
      Article.objects.filter(content='내용3') # content가 내용3인 모든 데이터
    ```

<br/>

## 참고
- QuerySet API 관련 문서
  - https://docs.djangoproject.com/en/3.2/ref/models/querysets/
  - https://docs.djangoproject.com/en/3.2/topics/db/queries/
- Field lookups
  - 특정 레코드에 대한 조건을 설정하는 방법
  - QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨
  - https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups
  - 예시
    - ```python
        Article.objects.filter(content__contains='dj')
      ```
- ORM, QuerySetAPI를 사용하는 이유
  - 데이터베이스 쿼리를 `추상화`하여 Django 개발자가 데이터베이스와 직접 상호작용하지 않아도 되도록 함
  - 데이터베이스와의 결합도를 낮추고 개발자가 더욱 `직관적이고 생산적`으로 개발할 수 있도록 도움

<br/>

## ORM 예시 코드
- todos
```python
from django.db import models

class Todo(models.Model):
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)

"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""

Todo.objects.create(
    content = '실습 제출',
    priority = 5,
    completed = False,
    deadline = timezone.now().date()
)

"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""

Todo.objects.create(
    content = '데일리 설문(오후) 제출',
    deadline = timezone.now().date()
)

"""
3. 임의의 할 일 5개 생성
"""

todos = [
    Todo(content='할일 1', priority='5', deadline=timezone.now().date() + timezone.timedelta(days=9)),
    Todo(content='할일 2', priority='4', deadline=timezone.now().date() + timezone.timedelta(days=7)),
    Todo(content='할일 3', priority='3', deadline=timezone.now().date() + timezone.timedelta(days=5)),
    Todo(content='할일 4', priority='2', deadline=timezone.now().date() + timezone.timedelta(days=3)),
    Todo(content='할일 5', priority='1', deadline=timezone.now().date() + timezone.timedelta(days=1))
]

Todo.objects.bulk_create(todos)

"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""

Todo.objects.order_by('pk')

"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""

Todo.objects.order_by('-pk')

"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""

Todo.objects.values().get(pk=1)
```

- newspaper
```python
from django.db import models

class Newspaper(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    journalist = models.CharField(max_length=80)
    created_at = models.DateField(auto_now_add=True)

"""
1. pk 필드가 1인 단일 데이터의 journalist 필드 조회
답 : Laney Mccullough
"""

Newspaper.objects.get(pk=1).journalist

"""
2. journalist 필드가 Laney Mccullough인 데이터 개수 조회
답 : 858
"""

Newspaper.objects.filter(journalist='Laney Mccullough').count()

"""
3. pk 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (10000)>, <Newspaper: Newspaper object (9999)>, ...생략
"""

Newspaper.objects.order_by('-pk')

"""
4. created_at 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (4719)>, <Newspaper: Newspaper object (97)>, ...생략
"""

Newspaper.objects.order_by('-created_at')

"""
5. journalist 필드가 Britney를 포함하는 데이터 개수 조회
답 : 799
"""

Newspaper.objects.filter(journalist__contains='Britney').count()

"""
6. journalist 필드가 ['Britney Mahoney', 'Arianna Walls', 'Carl Short']에 속하는 데이터 개수 조회
답 : 2469
"""

Newspaper.objects.filter(journalist__in=['Britney Mahoney', 'Arianna Walls', 'Carl Short']).count()

"""
7. created_at 필드가 2000-01-01 이후 데이터 개수 조회
답 : 4355
"""

Newspaper.objects.filter(created_at__gte='2000-01-01').count()

"""
8. 마지막 단일 데이터의 title, content, journalist 필드를 조회하고 아래와 같은 형식으로 출력
답
title : Teach father within million consumer baby its.
content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
Hand receive agree science present main. Other member every.
journalist : Laney Mccullough
"""

last = Newspaper.objects.values('title','content','journalist').last()
for key,value in last.items():
    print(f'{key} : {value}')

"""
기타 ORM 코드 작성 후 해당 코드와 결과 코드 리뷰 시간에 공유
"""

# 가장 최근에 작성된 데이터 5개의 title들을 조회
recent = Newspaper.objects.order_by('-created_at')[:5].values()
for i in recent:
    print(i['title'])
```