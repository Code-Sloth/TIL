# 장고 TIP

<br/>

### Select 필드
- ```html
    <!-- 보이는 데이터를 출력 -->
    {{ comment.get_category_display }}
  ```

<br/>

### Intcomma(가격 나타낼 때 사용)
- ```html
    <!-- settings.py에 humanize추가 후 -->

    {% load humanize %}

    {{ course.price|intcomma }}
  ```

<br/>

### model created_time
- ```python
    @property
    def created_time(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return self.created_at.strftime('%Y-%m-%d')
  ```