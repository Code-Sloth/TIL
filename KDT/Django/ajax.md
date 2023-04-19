# Django - django with Ajax

<br/>

## 개요
- 비동기(Asynchronous)
  - 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것(병렬적 수행)
  - 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
  - ex
    - Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 뒤에서 처리됨
    - ```javascript
        function slowRequest(callback) {
          console.log('1. 오래 걸리는 작업 시작...')
          setTimeout(function () {
            callback()
          }, 3000)
        }

        function myCallBack() {
          console.log('2. 콜백함수 실행됨')
        }

        slowRequest(myCallBack)
        console.log('3. 다른 작업 실행')

        // 출력결과
        // 1. 오래 걸리는 작업 시작 ...
        // 3. 다른 작업 실행
        // 2. 콜백함수 실행됨 
      ```

<br/>

### Ajax (Aynchronous JavaScript And XML)
- 비동기적인 웹 애플리케이션 개발을 위한 프로그래밍 기술명
- 사용자의 요청에 대한 즉각적인 반응을 제공하면서, 페이지 전체를 다시 로드하지 않고 `필요한 부분만` 업데이트 하는 것을 목표
- ex / Google Earth
- XMLHttpRequest
  - JavaScript 객체로, 클라이언트와 서버 간에 데이터를 비동기적으로 주고받을 수 있도록 해주는 객체
  - JavaScript 코드에서 서버에 요청을 보내고, 서버로부터 응답을 받을 수 있음
  - 문서를 매번 받는다 x 문서를 다시 그린다 o

<br/>

## 비동기 요청
- Axios
  - JavaScript에서 HTTP 요청을 보내는 라이브러리
  - python에서의 requests와 유사
  - 주로 프론트엔드 프레임워크에서 사용
  - 기본 문법
    - ```javascript
        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        <script>
          axios({
            method: 'HTTP 메서드',
            url: '요청 URL',
          })
            .then(성공하면 수행할 콜백함수)
            .catch(실패하면 수행할 콜백함수)
        </script>

        // 문법상 띄어놓는 것을 허용, 실제로는 한 줄의 코드
        // get,post등 여러 method 사용가능
        // then을 이용해서 성공하면 수행할 로직을 작성
        // catch를 이용해서 실패하면 수행할 로직을 작성
      ```

<br/>

### 고양이 사진 가져오기
- python
  - ```python
      # cat_api.py

      import requests
      # pip install requests

      print('고양이는 야옹')

      cat_image_search_url = 'https://api.thecatapi.com/v1/images/search'
      response = requests.get(cat_image_search_url)

      if response.status_code == 200:
        print(response.json())
      else:
        print('실패')

      print('야옹')

      # 출력
      # 고양이는 야옹
      # [{'id': 'bg6', 'url': 'https://cdn2.thecatapi.com/images/bg6.jpg', 'width': 500, 'height': 333}]
      # 야옹야옹
    ```
- JavaScript
  - ```javascript
      <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
      <script>
        console.log('고양이는 야옹')
        const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'

        axios({
          method: 'get',
          url: catImageSearchURL,
        })
          .then((response) => {
            console.log(response.data)
          })
          .catch((error) => {
            console.log('실패')
          })
        console.log('야옹야옹')
      </script>

      // 출력
      // 고양이는 야옹
      // 야옹야옹
      // 0: {id: 'e3b', url: 'https://cdn2.thecatapi.com/images/e3b.jpg', width: 600, height: 750}
    ```
- 결과 비교
  - `동기식 코드(python)`는 위에서부터 순서대로 처리가 되기때문에 첫번째 print가 출력되고 이미지를 가져오는 처리를 기다렸다가 다음 print가 출력됨
  - `비동기식 코드(JavaScript)`는 바로 처리가 가능한 작업(console.log)은 바로 처리하고, 오래 걸리는 작업인 이미지를 요청하고 가져오는 일은 요청을 보내놓고 기다리지 않고 다음 코드로 진행 후 완료가 된 시점에 결과 출력이 진행됨
- JavaScript 완성본
  - 참고
  - ```javascript
      <button>야옹이 버튼</button>

      <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
      <script>
        const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
        const btn = document.querySelector('button')

        btn.addEventListener('click', function () {
          axios({
            method: 'get',
            url: catImageSearchURL,
          })
            .then((response) => {
              imgElem = document.createElement('img')
              imgElem.setAttribute('src', response.data[0].url)
              document.body.appendChild(imgElem)
            })
            .catch((error) => {
              console.log('실패')
            })
        })
      </script>
    ```

<br/>

## 팔로우 with ajax
- 팔로우 구현
    - ```html
        <!-- accounts/profile.html -->

        <!-- 요소 선택을 위해 id 속성 지정 -->
        <div>
          팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span> / 
          팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span>
        </div>

        <!-- form선택할 수 있는 id지정, 유저의 pk를 전달하기 위한 방법 -->
        <form id='follow-form' data-user-id="{{ person.pk }}">
          {% csrf_token %}
          {% if request.user in person.followers.all %}
            <input type="submit" value="언팔로우">
          {% else %}
            <input type="submit" value="팔로우">
          {% endif %}
        </form>
        
        <!-- axios홈페이지 > jsDelivr CDN 사용하기 복사 -->
      ```
    - ```javascript
        // accounts/profile.html

        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        <script>
          // 폼 선택
          const form = document.querySelector('#follow-form')
          // 토큰 선택
          const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

          form.addEventListener('submit', function (event) {

            // 이벤트 기본 동작 취소
            event.preventDefault()

            // HTML로부터 전달받은 프로필 유저의 pk
            // data-* : HTML과 DOM사이에서 데이터를 교환할 수 있는 방법
            const userId = event.target.dataset.userId

            // axios로 요청 보내기
            axios({
              method: 'POST',
              url: `/accounts/${userId}/follow/`,
              headers: {'X-CSRFToken': csrftoken},
            })
              .then((response) => {
                // console.log(response.data.is_followed)
                const isFollowed = response.data.is_followed
                const followBtn = document.querySelector('#follow-form > input[type=submit]')

                if (isFollowed == true) {
                  // 현재 팔로우 > 버튼을 언팔로우로 조작
                  followBtn.value = '언팔로우'
                } else {
                  // 현재 언팔로우 > 버튼을 팔로우로 조작
                  followBtn.value = '팔로우'
                }

                // 팔로우 수 태그 선택
                const followingCountTag = document.querySelector('#followings-count')
                const followerCountTag = document.querySelector('#followers-count')

                // view에서 받은 팔로우 수
                const followingsCountData = response.data.followings_count
                const followersCountData = response.data.followers_count

                // 선택한 span태그의 내용을 팔로잉과 팔로워 수 데이터로 채워넣기

                followingCountTag.textContent = followingsCountData
                followerCountTag.textContent = followersCountData
              })
          })
        </script>
      ```
    - ```python
        # accounts/views.py

        @login_required
        def follow(request, user_pk):
            User = get_user_model()
            you = User.objects.get(pk=user_pk)
            me = request.user

            if you != me:
                if me in you.followers.all():
                    you.followers.remove(me)
                    is_followed = False # 버튼을 바꿔줄 변수
                else:
                    you.followers.add(me)
                    is_followed = True
                context = {
                    'is_followed': is_followed,
                    'followings_count': you.followings.count(), # 팔로우 수 갱신
                    'followers_count': you.followers.count(),
                }
                return JsonResponse(context)
            return redirect('accounts:profile', you.username, context)
      ```

<br/>

## 좋아요 with ajax
- 팔로우와 동일한 흐름 + forEach() + querySelectorAll()
- index페이지 각 게시글에 각각 좋아요 버튼이 있기 때문에 반복 + 목록 선택
    - ```html
        <!-- articles/index.html -->

        <form class="like-forms" data-article-id="{{ article.pk }}">
          {% csrf_token %}
          {% if request.user in article.like_users.all %}
            <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
          {% else %}
            <input type="submit" value="좋아요" id="like-{{ article.pk }}">
          {% endif %}
        </form>
      ```
    - ```python
        # articles/views.py

        from django.http import JsonResponse

        @login_required
        def likes(request, article_pk):
            article = Article.objects.get(pk=article_pk)

            if request.user in article.like_users.all():
                article.like_users.remove(request.user)
                is_liked = False
            else:
                article.like_users.add(request.user)
                is_liked = True
            context = {
                'is_liked': is_liked,
            }
            return JsonResponse(context)
      ```
    - ```javascript
        // articles/index.html

        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        <script>
          const forms = document.querySelectorAll('.like-forms')
          const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

          forms.forEach((form) => {
            form.addEventListener('submit', function (event) {
              event.preventDefault()
              const articleId = event.target.dataset.articleId
              axios({
                method: "POST",
                url: `http://127.0.0.1:8000/articles/${articleId}/likes/`,
                headers: {'X-CSRFToken': csrftoken},
              })
                .then((response) => {
                  const isLiked = response.data.is_liked
                  const likeBtn = document.querySelector(`#like-${articleId}`)
                  if (isLiked === true) {
                    likeBtn.value = '좋아요 취소'
                  } else {
                    likeBtn.value = '좋아요'
                  }
                })
                .catch((error) => {
                  console.log(error.response)
                })
            })
          })
        </script>
      ```

<br/>

## 참고
- 비동기를 사용하는 이유 : 사용자 경험
  - 예를 들어 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때, 동기로 처리한다면 데이터를 모두 불러온 뒤에야 앱의 실행 로직이 수행되므로 사용자들은 마치 앱이 멈춘 것과 같은 경험을 겪게 됨
  - 즉, 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨
  - 비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로, 사용자 경험에 긍정적인 효과를 볼 수 있음
  - 이와 같은 이유로 많은 웹 기능은 비동기 로직을 사용해서 구현되어 있음
