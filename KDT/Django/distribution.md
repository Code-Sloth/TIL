# 배포

</br>

## 클라우드 타입 배포
- `$ pip install python-dotenv`
- `$ pip freeze > requirements.txt`
- .env 파일 생성
  - ```
      SECRET_KEY = 'DQENER315qrln352adf12ndgf'
    ```
- settings.py
  - ```python
      # SECRET_KEY 삭제

      import os
      from dotenv import load_dotenv

      load_dotenv()
      SECRET_KEY = os.getenv('SECRET_KEY')
    ```
- 내 GitHub 저장소 배포하기
- 언어 프레임웍
  - Python DJango
- 리전
  - Seoul-Korea
- SECRET_KEY 입력
- API_KEY 입력
- DJANGO_SUPERUSER_USERNAME : 관리자 아이디
- DJANGO_SUPERUSER_EMAIL : 관리자 이메일
- DJANGO_SUPERUSER_PASSWORD : 관리자 비밀번호
- 더 많은 옵션
  - Pre start Commend : python manage.py migrate && python manage.py createsuperuser --noinput
  - 필요하면 loaddata 명령어 추가
- 배포 완료 후 오류창에서 URL복사
- settings의 ALLOWED_HOSTS에 입력
