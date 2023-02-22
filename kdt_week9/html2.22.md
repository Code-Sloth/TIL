# Web

<br/>

## Web
- World Wide Web
  - 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간
- Web site
  - 인터넷에서 여러 개의 Web page가 모인 것으로 사용자들에게 정보나 서비스를 제공하는 공간
- Web page
  - HTML, CSS, JavaScript 등의 웹 기술을 이용하여 만들어진, 하나의 인터넷 문서

<br/>

## HTML(HyperTextMarkUp Language)
- 웹 페이지의 의미와 구조를 정의하는 언어
- Hypertext
  - 웹 페이지를 다른 페이지로 연결하는 링크
  - 참조를 통해 사용자가 한 문서에게 다른 문서로 즉시 접근할 수 있는 텍스트

<br/>

### HTML 구조
```html
<p>content</p>
```
- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성
- 닫는 태그는 태그 이름 앞에 슬래시가 포함되어 닫는 태그가 없는 태그도 존재

<br/>

### HTML 속성
- 규칙
  - 요소 이름 다음에 바로 오는 속성은 요소 이름과 속성 사이에 공백이 존재해야함
  - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분
  - 속성 값은 열고 닫는 따옴표로 감싸야 함
- 목적
  - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
  - CSS가 해당 요소를 선택하기 위한 값으로 활용

<br/>

### HTML 문서의 구조

- ```html
  <!DOCTYPE html>
  해당 문서가 html로 문서라는 것을 나타냄
  ```

- ```html
  <html></html>
  전체 페이지의 콘텐츠를 포함
  ```

- ```html
  <title></title>
  브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
  ```

- ```html
  <head></head>
  HTML 문서에 관련된 설명, 설정 등
  사용자에게 보이지 않음
  ```

- ```html
  <body></body>
  페이지에 표시되는 모든 콘텐츠
  ```

- ```html
  <h1></h1>
  문서의 최상위 제목, 텍스트 크기 최대
  ```

- ```html
  <ol><li></li></ol>
  1., 2., 3.으로 정렬된 목록
  ```

- ```html
  <ul><li></li></ul>
  -으로 정렬되지 않은 목록
  ```

- ```html
  <em></em>
  기울임체
  ```

- ```html
  <strong></strong>
  굵은 글씨체
  ```

<br/>

## CSS(Cascading Style Sheet)
- 웹 페이지의 디자인과 레이아웃을 구성하는 언어
- ```html
  <h1>
    color: blue; 
    font-size: 15px;
  </h1>
  ```
  h1 = 선택자
  color: blue; = 선언
  font-size = 속성
  15px = 값

<br/>

### CSS 적용 방법
- 인라인 스타일
  - ```html
    <h1 style="color:blue;">hello world!</h1>
    ```
- 내부 스타일 시트
  - ```html
    <style>
      h1 {
        color:blue;
      }
    </style>
    ```
- 외부 스타일 시트
  - ```html
    <link rel="stylesheet" href="style.css">

    h1 {
      color: blue;
    }
    ```
  별도의 CSS파일 생성 후 불러오기

<br/>

## Select elements

<br/>

### CSS Selectors
- HTML 요소를 선택하여 스타일을 적용할 수 있게 함
- 기본 선택자
  - 전체(*) 선택자
  - 요소(tag) 선택자
    - 지정한 모든 태그를 선택
  - 클래스(class) 선택자
    - 주어진 클래스 속성을 가진 모든 요소를 선택
  - 아이디(id) 선택자
    - 주어진 아이디 속성을 가진 요소 선택
    - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
  - 속성(attr) 선택자
- 결합자
  - 자손 결합자(""(space))
    - 첫 번째 요소의 자손 요소들 선택
  - 자식 결합자(>)
    - 첫 번째 요소의 직계 자식만 선택
    
<br/>

## Cascade & Specificity
- 계단식 & 우선 순위
- 동일한 요소에 적용 가능한 같은 스타일을 두가지 이상 작성 했을 때 어떤 규칙이 이기는지 결정하는 것
- Cascade(계단식)
  - 동일한 우선순위를 갖는 규칙이 적용될 때 CSS에서 마지막에 나오는 규칙이 사용
- Specificity
  - 선택자 별로 정해진 우선순위 점수에 따라 점수가 높은 규칙이 사용
- 우선 순위
  1. !important
  2. 인라인 스타일
  3. id 선택자
  4. class 선택자
  5. 요소 선택자
  6. 소스 코드 순서

<br/>

## 참고
- HTML
  - 요소 이름은 소문자 사용을 권장
  - 속성 따옴표는 큰 따옴표를 권장
  - 프로그래밍 언어와 달리 에러를 반환하지 않음
- CSS
  - 인라인 스타일은 유지보수가 힘들기 때문에 사용 지양
  - 모든 속성을 외우는 게 아닌 주로 활용하는 속성 위주로 학습
  - 속성은 되도록 class만 사용
  - CSS 상속 여부는 MDN 문서에서 확인
- 구글 검색 시 MDN 문서를 위주로 확인

<br/>

### 예제 코드
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset = "UTF-8">
  <title>컨텐츠</title>
  <style>
    h1 {
      color: blue; /*요소 선택자 : 지정한 모든 태그*/
    }

    .make-red {
      color: red; /*클래스 선택자 : 주어진 클래스 속성을 가진 모든 요소*/
    }

    #make-purple {
      color: purple; /*아이디 선택자 : 주어진 아이디를 가진 요소가 하나만 */
    }
  </style>
</head>
<body>
  안녕하세요.
  <br/>
  반갑습니다.
  <p class="make-red">This is my page!!!</p>
  <a href="https://www.google.co.kr/">구글로 이동!</a>
  <img src="wealthy.jpg" alt="웰시코기 사진">
  <img src="https://random.imagecdn.app/500/150" alt="">
  <h1>메인 제목</h1>
  <h1>또 다른 h1 태그</h1>
  <h2 class="make-red">중제목</h2>
  <p id="make-purple">내 페이지</p>
  <p>이건 <em class="make-red">emphasis</em> 입니다.</p>
  <p>이건 <strong>strong</strong> 입니다.</p>
  <em>테스트</em>
  <ol>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>DB</li>
  </ol>
</body>
</html>

```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    * {
      color: red;
    }

    h2 {
      color: orange;
    }

    h3,
    h4 {
      color: blue;
    }

    .green {
      color: green;
    }

    #purple {
      color: purple;
    }

    /* 자식 결합자 */
    .green > span {
      font-size: 50px;
    }

    /* 자손 결합자 */
    .green li {
      color: brown;
    }

  </style>
</head>
<body>
  <h1 class="green">Heading</h1>
  <h2>선택자 연습</h2>
  <h3>헬로</h3>
  <h4>반가워요</h4>
  <p id="purple">과목 목록</p>
  <ul class="green">
    <li>파이썬</li>
    <li>알고</li>
    <li>웹
      <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>JS</li>
      </ol>
    </li>
  </ul>
  <p class="green">Lorem, <span>ipsum</span> dolor.</p>
</body>
</html>

<!-- 검색할 때 mdn 붙이기 -->

```