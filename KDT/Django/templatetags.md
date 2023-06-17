# Django Templatetags

<br/>

### 생성
- templatetags 폴더 생성
- _ _init__.py 파일 생성
- <파일 이름>.py 생성 ex/ customtags.py

<br/>

### customtags.py
- ```python
    # 방법 1
    from django import template

    register = template.Library()

    def string_kr(value):
        if value == 'traditional':
            return '전통주'
        elif value == 'beer':
            return '맥주'

    register.filter('string_kr',string_kr)

    # 방법 2
    from django import template

    register = template.Library()

    @register.simple_tag
    def string_kr(value):
        if value == 'traditional':
            return '전통주'
        elif value == 'beer':
            return '맥주'
        
    # 폼도 가능
    from django import template
    from ..forms import CommentForm
    from communities.forms import CommentForm as CommunitiesCommentForm

    register = template.Library()

    def get_comment_update_form(comment):
        comment_update_form = CommentForm(instance=comment)
        return comment_update_form

    register.filter('get_comment_update_form', get_comment_update_form)
  ```

<br/>

### html
- ```html
    {% load customtags %}

    <!-- 방법 1 -->
    {{ product.category|string_kr }}

    <!-- 방법 2 -->
    {{ string_kr product.category }}

    <!-- 폼 -->
    {{ comment|get_comment_update_form|safe }}
  ```