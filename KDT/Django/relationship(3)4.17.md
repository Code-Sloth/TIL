# Django - Many to many relationships 1

<br/>

## 개요
- M:N 관계
  - 병원 진료 시스템 모델 관계 만들기(환자-의사)
- N:1 관계의 한계
  - 1명의 의사에게 여러 환자가 예약할 수 있다고 모델 관계를 설정
    - ```python
        # hospitals/models.py

        from django.db import models

        class Doctor(models.Model):
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 의사 {self.name}'

        class Patient(models.Model):
            doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 환자 {self.name}'
      ```
  - 각각 2명의 의사와 환자를 생성하고 환자는 서로 다른 의사에게 예약했다고 가정
    - ```python
        # shell_plus

        doctor1 = Doctor.objects.create(name='alice')
        doctor2 = Doctor.objects.create(name='bella')
        patient1 = Patient.objects.create(name='carol', doctor=doctor1)
        patient2 = Patient.objects.create(name='dane', doctor=doctor2)
        patient3 = Patient.objects.create(name='carol', doctor=doctor2)
        # 여기서 carol은 id가 1이지만 2번 의사에 연결하기 위해 id가 3으로 또 객체를 생성해서 문제가 발생
        patient4 = Patient.objects.create(name='dane', doctor=doctor1, doctor2)
        # 외래 키 컬럼에 '1,2'형태로 참조한느 것은 Integer 타입이 아니기 때문에 동시예약 불가능
      ```
- 중개 모델
  - 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 작성
  - 예약 모델은 의사와 환자에 각각 N:1관계를 가짐
    - ```python
        # hospitals/models.py

        from django.db import models

        class Doctor(models.Model):
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 의사 {self.name}'

        # 외래키 삭제
        class Patient(models.Model):
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 환자 {self.name}'

        # 중개모델 작성
        class Reservation(models.Model):
            doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
            patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

            def __str__(self):
                return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
      ```
  - 의사와 환자 생성 후 예약 만들기
    - ```python
        # shell_plus

        doctor1 = Doctor.objects.create(name='alice')
        patient1 = Patient.objects.create(name='carol')

        Reservation.objects.create(doctor=doctor1, patient=patient1)

        doctor1.reservation_set.all()
        # 1번 의사의 1번 환자
        patient1.reservation_set.all()
        # 1번 의사의 1번 환자

        patient2 = Patient.objects.create(name='dane')
        Reservation.objects.create(doctor=doctor1, patient=patient2)
        # 1번 의사의 1번 환자, 1번 의사의 2번 환자
      ```

<br/>

### 의사 환자 관계 : ManyToManyField
- 환자 모델에 Django ManyToManyField 작성
  - ```python
      # hospitals/models.py

      from django.db import models

      class Doctor(models.Model):
          name = models.TextField()

          def __str__(self):
              return f'{self.pk}번 의사 {self.name}'

      class Patient(models.Model):
          # ManyToManyField 작성
          doctors = models.ManyToManyField(Doctor)
          name = models.TextField()

          def __str__(self):
              return f'{self.pk}번 환자 {self.name}'

      # 위에서 작성한 중개 테이블이 자동으로 생성
    ```
- 의사 1명과 환자 2명 생성
  - ```python
      # shell_plus

      doctor1 = Doctor.objects.create(name='alice')
      patient1 = Patient.objects.create(name='carol')
      patient2 = Patient.objects.create(name='dane')

      # 환자가 의사에게 예약

      patient1.doctors.add(doctor1)
      # 환자1이 의사1에게 예약
      patient1.doctors.all()
      # 1번 의사 alice
      doctor1.patient_set.all()
      # 1번 환자 carol

      # 의사가 환자를 예약

      doctor1.patient_set.add(patient2)
      # 의사1이 환자2를 예약
      doctor1.patient_set.all()
      # 1번 환자 carol, 2번 환자 dane
      patient2.doctors.all()
      # 1번 의사 alice
      patient1.doctors.all()
      # 1번 의사 alice

      doctor1.patient_set.remove(patient1)
      # 의사1이 환자1 예약 취소
      doctor1.patient_set.all()
      # 2번 환자 dane
      patient1.doctors.all()
      # 빈 QuerySet

      patient2.patient_set.remove(doctor1)
      # 환자2가 의사1 예약 취소
      patient2.doctors.all()
      # 빈 QuerySet
      doctor1.patient_set.all()
      # 빈 QuerySet
    ```
- `동등한 관계`이기 때문에 어디에 추가하든 상관없고 참조, 역참조만 고려
- through argument
  - 중개 테이블을 수동으로 지정하려는 경우 `through` 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django모델을 지정할 수 있음
  - 가장 일반적인 용도는 중개 테이블에 추가 데이터를 사용해 N:M관계와 연결하려는 경우
  - through 설정 및 Reservation Class 수정
  - 예약 정보에 '증상'과 '예약일'이라는 추가 데이터 생성
    - ```python
        # hospitals/models.py

        from django.db import models

        class Doctor(models.Model):
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 의사 {self.name}'

        class Patient(models.Model):
            doctors = models.ManyToManyField(Doctor, through='Reservation')
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 환자 {self.name}'

        class Reservation(models.Model):
            doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
            patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
            symptom = models.TextField() 
            # 증상
            reserved_at = models.DateTimeField(auto_now_add=True)
            # 예약일

            def __str__(self):
                return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
      ```
  - 의사 1명과 환자 2명 생성
    - ```python
        # shell_plus

        doctor1 = Doctor.objects.create(name='alice')
        patient1 = Patient.objects.create(name='carol')
        patient2 = Patient.objects.create(name='dane')

        # 1. Reservation class를 통한 예약 생성
        reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
        reservation1.save()
        doctor1.patient_set.all()
        # 1번 환자 carol
        patient1.doctors.all()
        # 1번 의사 alice

        # 2. Patient 객체를 통한 예약 생성
        patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
        doctor1.patient_set.all()
        # 1번 환자 carol, 2번 환자 dane
        patient2.doctors.all()
        # 1번 의사 alice

        # 예약 삭제
        doctor1.patient_set.remove(patient1)
        patient2.doctors.remove(doctor1)
      ```
- 정리
  - M:N 관계로 맺어진 두 테이블에는 변화가 없음
  - ManyToManyField는 `중개 테이블`을 자동으로 생성함
  - ManyToManyField는 M:N관계를 맺는 두 모델 어디에 위치해도 상관 없음
  - 대신 필드 작성 위치에 따라 `참조 역참조 방향`을 주의
  - N:1은 완전한 종속 관계였지만 M:N은 M의 N, N의 M 두가지 형태로 모두 표현이 가능(동등한 관계)

<br/>

## ManyToManyField
- ManyToManyField(to, **options)
  - many-to-many 관계 설정 시 사용하는 모델 필드
  - 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 생성
    - add(), remove(), create(), clear() ...
- ManyToManyField's Arguments
  - related_name
    - 역참조 시 사용하는 manager name을 변경
      - ```python
          class Patient(models.Model):
            doctors = models.ManyToManyField(Doctor, related_name='patients')
            name = models.TextField()
          
          # 변경 전
          doctor.patient_set.all()
          # 변경 후
          doctor.patients.all()
        ```
  - through
    - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정
    - 일반적으로 중개 테이블에 추가 데이터를 사용하는 N:M 관계와 연결하려는 경우(extra data with a many-to-many relationship)에 사용됨
  - symmetrical
    - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
    - 기본 값: True
      - ```python
          # ex 1) self와 symmetrical=True인 경우

          class User(models.Model):
            name = models.CharField(max_length=100)
            friends = models.ManyToManyField('self')
          
          # 사용자 생성
          user1 = User.objects.create(name='John')
          user2 = User.objects.create(name='Mike')
          user3 = User.objects.create(name='Alice')

          # 사용자와 친구 관계 설정
          user1.friends.add(user2)
          user1.friends.add(user3)
          user2.friends.add(user3)

          # 사용자와 친구 관계 확인
          user1.friends.all()  # <QuerySet [<User: Mike>, <User: Alice>]>
          user2.friends.all()  # <QuerySet [<User: John>, <User: Alice>]>
          user3.friends.all()  # <QuerySet [<User: John>, <User: Mike>]>

          # ex 2) self와 symmetrical=False인 경우

          class User(models.Model):
            name = models.CharField(max_length=100)
            friends = models.ManyToManyField('self', symmetrical=False)

          # 사용자와 친구 관계 설정
          user1.friends.add(user2)

          # 사용자와 친구 관계 확인
          user2.friends.all()  # <QuerySet []>
        ```
    - True일 경우
      - `_set` 매니저를 추가하지 않음
      - source모델의 인스턴스가 target모델의 인스턴스를 참조하면 자동으로 target모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함`(대칭)`
      - 즉, 내가 당신의 친구라면 당신도 내 친구가 됨
    - 대칭을 원하지 않는 경우 False로 설정
      - Follow기능 구현에서 다시 확인
- M:N에서의 methods
  - `add()`
    - 지정된 객체를 관련 객체 집합에 추가
    - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
  - `remove()`
    - 관련 객체 집합에서 지정된 모델 개체를 제거

<br/>

## Article & User
- Many to many relationships
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
  - 양쪽 모두에서 N:1 관계를 가짐
- Article(M) - User(N)
  - 0개 이상의 게시글은 0명 이상의 회원과 관련됨
  - 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있음
- 모델 관계 설정
  - ManyToManyField 작성
    - ```python
        class Article(models.Model):
          user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
          like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
          title = models.CharField(max_length=10)
          content = models.TextField()
          created_at = models.DateTimeField(auto_now_add=True)
          updated_at = models.DateTimeField(auto_now=True)
      ```
    - 위의 코드는 오류가 발생
      - like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성
      - 그러나 이전 N:1(Article-User)관계에서 이미 해당 매니저를 사용 중
      - user가 작성한 글들(user.article_set)과 user가 좋아요를 누른 글(user.article_set)을 구분할 수 없음
      - user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 `related_name`을 작성해야 함
      - ```python
          like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
        ```
    - User-Article간 사용 가능한 related manager 정리
      - article.user
        - 게시글을 작성한 유저 N:1
      - user.article_set
        - 유저가 작성한 게시글(역참조) N:1
      - article.like_users
        - 게시글을 좋아요한 유저 M:N
      - user.like_articles
        - 유저가 좋아요한 게시글(역참조) M:N
  - `좋아요` 구현
    - ```python
        # articles/urls.py

        urlpatterns = [
          ...
          path('<int:article_pk>/likes/', views.likes, name='likes'),
        ]

        # articles/views.py

        @login_required
        def likes(request, article_pk):
          article = Article.objects.get(pk=article_pk)
          if request.user in article.like_users.all():
            article.like_users.remove(request.user)
          else:
            article.like_users.add(request.user)
          return redirect('articles:index')
      ```
    - ```html
        <!-- articles/index.html -->

        {% for article in articles %}
          ...
          <form action="{% url 'articles:likes' article.pk %}" method="POST">
            {% csrf_token %}
            {% if request.user in article.likes_users.all %}
              <input type="submit" value="좋아요 취소">
            {% else %}
              <input type="submit" value="좋아요">
            {% endif %}
          </form>
        {% endfor %}
      ```

<br/>

## 참고
- `.exists()`
  - QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
  - 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용 (속도 개선)
  - exists 적용
    - ```python
        # articles/views.py

        @login_required
        def likes(request, article_pk):
          article = Article.objects.get(pk=article_pk)
          if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
          else:
            article.like_users.add(request.user)
          return redirect('articles:index')
      ```
