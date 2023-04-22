# Django - Paginator

<br/>

## Paginator
- ```python
    # articles/views.py

    from django.core.paginator import Paginator


    def index(request):
        articles = Article.objects.order_by('-pk')
        """
          [int] page
          현재 주소의 페이지 번호를 할당받는 변수
          주소에 page(키)에 대한 값이 없으면 1 할당
        """
        page = request.GET.get('page', '1')

        """
          [int] per_page
          페이지를 나누는 기준
          e.g. 10 -> 데이터를 10개를 기준으로 나눔.
        """
        per_page = 5

        """
          [Paginator 인스턴스] paginator
          첫 번째 인자 : 페이지네이션을 적용할 데이터(queryset)
          두 번째 인자 : per_page
        """
        paginator = Paginator(articles, per_page)

        """
          [Page 인스턴스] page_obj
          출력할 데이터 및 페이지네이션을 구현을 위한 데이터가 저장된 변수
          반복문으로 순회하면 페이징 처리가 된 데이터가 요소가 됨.
        """
        page_obj = paginator.get_page(page)

        """
          제일 마지막으로 이동하기 위한 변수 설정
        """

        last = paginator.num_pages

        context = {
            'articles': page_obj,
            'last': last,
        }
        return render(request, 'articles/index.html', context)
  ```
  ```html
    <!-- articles/indes.html -->

      <!-- 페이지네이션 컴포넌트 시작 -->
      <ul class="pagination justify-content-center">
        
        <!-- 이전 페이지 버튼 -->
        <!-- 이전 페이지가 존재할 경우 이전 페이지 버튼 활성화 -->
        {% if articles.has_previous %}
          <li class="page-item">
            <a class="page-link" href="?page=1">처음</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="?page={{ articles.previous_page_number }}">이전</a>
          </li>
        {% else %}
          <li class="page-item disabled">
            <a class="page-link" tabindex="-1" aria-disabled="true" href="#">처음</a>
          </li>
          <li class="page-item disabled">
            <a class="page-link" tabindex="-1" aria-disabled="true" href="#">이전</a>
          </li>
        {% endif %}

        <!-- 페이지 번호 리스트 생성 반복문 -->
        {% for page_number in articles.paginator.page_range %}

          
          <!-- 페이지 번호가 무한히 생성되는 것을 막는 조건문 -->
          <!-- 현재 페이지에서 +- 5 까지 생성 -->
          {% if page_number >= articles.number|add:-5 and page_number <= articles.number|add:5 %}
            {% if page_number == articles.number %}
              <li class="page-item active" aria-current="page">
                <a class="page-link" href="?page={{ page_number }}">{{ page_number }}</a>
              </li>
            {% else %}
              <li class="page-item">
                <a class="page-link" href="?page={{ page_number }}">{{ page_number }}</a>
              </li>
            {% endif %}
          {% endif %}
        {% endfor %}

        <!-- 다음 페이지 버튼 -->
        <!-- 다음 페이지가 존재할 경우 다음 페이지 버튼 활성화 -->
        {% if articles.has_next %}
          <li class="page-item">
            <a class="page-link" href="?page={{ articles.next_page_number }}">다음</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="?page={{ last }}">마지막</a>
          </li>
        {% else %}
          <li class="page-item disabled">
            <a class="page-link" tabindex="-1" aria-disabled="true" href="#">다음</a>
          </li>
          <li class="page-item disabled">
            <a class="page-link" tabindex="-1" aria-disabled="true" href="#">마지막</a>
          </li>
        {% endif %}
      </ul>
  ```