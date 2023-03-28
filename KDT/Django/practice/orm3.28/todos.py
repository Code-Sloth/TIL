from django.db import models

# Create your models here.

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