# Form

<br/>

## 개요
- HTML form
  - 사용자로부터 form 요소를 통해 데이터를 받고 있으니 비정상적 혹은 악의적인 요청을 확인하지 않고 모두 수용중
  - 우리가 원하는 데이터 형식이 맞는지에 대한 유효성 검증 필요
- 유효성 검사
  - 수집한 데이터가 정확하고 유효한지 확인하는 과정
  - 유효성 검증에는 입력 값, 형식, 중복, 범위, 보안 등 부가적인 많은 것들을 고려해야 함
  - 이런 과정과 기능을 제공해주는 도구가 필요

<br/>

## Django Form
- 사용자 입력 데이터를 수집하고 처리 및 유효성 검증을 수행하기 위한 도구
- 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공
- ```python
    # articles/forms.py

    class ArticleForm(forms.Form):
      title = forms.CharField(max_length=10)
      content = forms.CharField()
  ```
  ```python
    # articles/views.py

    from .forms import ArticleForm

    def new(request):
      form = ArticleForm()
      context = {
          'form' : form
      }
      return render(request, 'articles/new.html', context)
  ```
  ```html
    <!-- articles/new.html -->

    <h1>New</h1>
    <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit">
    </form>
    <a href="{% url 'articles:index' %}">[back]</a>
  ```

<br/>

### Widgets
- HTML input element의 표현을 담당
- ```python
    class ArticleForm(forms.Form):
      title = forms.CharField(max_length=10)
      content = forms.CharField(widget=forms.Textarea)
  ```

<br/>

## Django ModelForm
- Form
  - 사용자 입력 데이터를 DB에 저장하지 않을 때 (ex 로그인)
- ModelForm
  - 사용자 입력 데이터를 DB에 저장해야 할 때 (ex 회원가입)

<br/>

### ModelForm Create 로직
- ```python
    # articles/forms.py

    from django import forms
    from .models import Article

    class ArticleForm(forms.ModelForm):
        class Meta: # ModelForm의 정보를 작성하는 곳
            model = Article
            fields = '__all__'
            # fields = ('title',) 타이틀만 나옴
            # exclude = ('title',) 타이틀을 제외
  ```
  ```python
    # articles/views.py

    def create(request):
      form = ArticleForm(request.POST)
      if form.is_valid():
          article = form.save()
          return redirect('articles:detail', article.pk)
      context = {
          'form' : form
      }
      return render(request, 'articles/new.html', context)
  ```
- is_valid()
  - 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환

<br/>

### ModelForm edit 로직
- ```python
    # articles/views.py

    def edit(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      form = ArticleForm(instance=article)
      context = {
          'article': article,
          'form' : form,
      }

      return render(request, 'articles/edit.html', context)
  ```
  ```html
    <!-- articles/edit.html -->

    <h1>Edit</h1>
    <form action="{% url 'articles:update' article.pk %}" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="[UPDATE]">
    </form>
  ```

<br/>

### ModelForm update 로직
- ```python
    # articles/views.py

    def update(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      form = ArticleForm(request.POST, instance=article)
      if form.is_valid():
          article = form.save()
          return redirect('articles:detail', article.pk)
      context = {
          'article' : article,
          'form' : form,
      }
      return render(request, 'articles/edit.html', context)
  ```
- save()
  - 데이터베이스 객체를 만들고 저장
  - 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지 결정

<br/>

## 참고
- ModelForm 키워드 인자 data와 instance
    - ```python
        class BaseModelForm(BaseForm):
          def __init__(
              self,
              data=None,
              files=None,
              auto_id="id_%s",
              prefix=None,
              initial=None,
              error_class=ErrorList,
              label_suffix=None,
              empty_permitted=False,
              instance=None,
              use_required_attribute=None,
              renderer=None,
          ):
      ```
- Widget 응용
    - ```python
        # articles/forms.py

        class ArticleForm(forms.ModelForm):
          title = forms.CharField(
              widget=forms.TextInput(
                  attrs= {
                      'class' : 'my-title',
                      'placeholder' : '제목을 입력해주세요.',
                  }
              )
          )
          class Meta:
              model = Article
              fields = ('__all__')
      ```
      ```python
        # articles/forms.py
        class ArticleForm(forms.ModelForm):
          title = forms.CharField(
              widget=forms.TextInput(
                  attrs= {
                      'class' : 'my-title',
                      'placeholder' : '제목을 입력해주세요.',
                      'maxlength' : 10,
                  }
              ),
          )
          content = forms.CharField(
              label = '내용',
              widget=forms.Textarea(
                  attrs={
                      'class' : 'my-content',
                      'placeholder' : 'Enter the content',
                      'rows' : 5,
                      'cols' : 50,
                  }
              ),
              error_messages={'required' : '내용을 입력해주세요.'},
          )

          class Meta:
              model = Article
              fields = ('__all__')
      ```
- Meta class
  - 파이썬안에서는 Inner class 혹은 Nested class
  - 파이썬의 문법적 개념으로 접근하지는 말 것
  - 단순히 모델 정보를 Meta라는 이름의 내부 클래스로 작성되도록 ModelForm의 설계가 이렇게 되어있을 뿐
  - ModelForm의 역할과 사용법을 숙지하는데 집중

<br/>

## view함수
- new & create
  - 공통점 : 데이터 생성 로직을 구현하기 위함
  - 차이점 : new는 GET method요청, create는 POST method요청만을 처리
- ```python
    # articles/views.py

    def newcreate(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)

      else:
          form = ArticleForm()

      context = {
          'form' : form
      }
      return render(request, 'articles/new.html', context)

      # (GET) articles/create/
      # (POST) articles/create/
  ```
- ```python
    # articles/views.py

    def update(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      if request.method == 'POST':
          form = ArticleForm(request.POST, instance=article)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)
          
      else:
          form = ArticleForm(instance=article)

      context = {
          'article' : article,
          'form' : form,
      }
      return render(request, 'articles/edit.html', context)

      # (GET) articles/update/
      # (POST) articles/update/
  ```
