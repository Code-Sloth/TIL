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
