# JavaScript

<br/>

## JavaScript 배경

<br/>

### 웹 브라우저의 상용화
- 1994년, Netscape사의 최초 상용 웹 브라우저인 Netscape Navigator 출시
- 당시 약 90% 이상의 시장 점유율을 가졌을 것이라 추정

<br/>

### 웹 브라우저 경쟁
- 1995년, Microsoft의 Internet Explorer(IE) 출시
- Netscape는 IE와 경쟁할 차기 웹 브라우저 개발을 착수
- 당시에는 웹 페이지에 동적인 기능이 없었기 때문에 Netscape는 웹 페이지의 동적인 기능을 제공하기 위한 새로운 언어를 개발하기 시작

<br/>

### JavaScript의 탄생
- 당시 Netscape소속 개발자 Brandon Eich는 회사의 요구사항을 넘어 Mocha라는 언어를 개발
- 이후 LiveScript로 이름을 변경했으나 당시 인기있던 프로그래밍 언어인 JAVA의 명성에 기대고자 JavaScript로 이름 변경
- JavaScript는 Netscape Navigator 2.0에 탑재되어 큰 인기를 누림

<br/>

### JavaScript의 파편화
- Microsoft는 JavaScript의 파생버전인 Jscript를 IE 3.0에 채택
- 이 과정에서 Netscape와 Microsoft 그리고 많은 회사들이 자체적으로 Javascript를 탑재해 독자적으로 업데이트
- 이로 인해 같은 코드가 브라우저 마다 다르게 동작하는 등의 문제가 발생

<br/>

### 1차 브라우저 전쟁
- Microsoft는 IE를 자사 윈도우 운영체제에 내장하여 무료로 배포
- 빌 게이츠를 필두로 한 Microsoft의 공격적인 마케팅, 자금력, 그리고 막강한 윈도우 운영체제 점유율 앞에 Netscape는 빠르게 몰락하기 시작
- 결국 IE의 시장 점유율은 2002년 96%에 달하며 Microsoft의 승리로 종료
- 이후 많은 브라우저들이 IE에 도전했지만 모두 실패

<br/>

### 2치 브라우저 전쟁
- 2008년 구글에서 Chrome 브라우저를 출시
- 출시 3년만에 10년간 쌓아온 Firefox의 점유율을 넘어섰고 그로부터 반년 뒤 IE의 점유율을 넘어섬
- 빠른 속도, 압도적인 성능, 엄격한 웹 표준 준수, 강력한 개발자 도구를 제공
- 웹 표준의 발전과 웹 애플리케이션의 대중화에 큰 역할

<br/>

### JavaScript 현황
- 현재는 Chrome, Firefox, Safari, Microsoft Edge등 다양한 웹 브라우저가 출시되어 있으며, 웹 브라우저 시장이 다양화
- 기존에 JavaScript는 브라우저에서만 웹 페이지의 동적인 기능을 구현하는 데 사용
- 이후 브라우저에서 벗어나 Node.js와 같은 서버 사이드 분야 뿐만 아니라, 다양한 프레임워크와 라이브러리들이 개발되면서, 웹 개발 분야에서는 필수적인 언어로 자리

<br/>

### JavaScript의 표준화
- ECMAScript
  - Ecma International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어
- JavaScript의 파편화를 막기 위해 1997년 ECMA에서 ECMAScript라는 표준 언어를 정의
- 이후 ECMAScript는 독자적으로 발전하며 JavaScript보다 더 많은 기능을 제공
- 2009년에는 ECMAScript 5 (ES5) 에서 안정성과 생산성을 크게 높임
- 2015년에는 ECMAScript 2015(ES6)에서 객체지향 프로그래밍 언어로써 많은 발전을 이루어, 역사상 가장 중요한 버전으로 평가됨
- JavaScript는 ECMAScript의 구현 언어 중 하나

<br/>

## JavaScript 언어

<br/>

### JavaScript 개요
- 웹 페이지의 동적인 기능을 구현하기 위한 웹 브라우저에서의 JavaScript를 학습
- 웹 브라우저에 내장된 JavaScript 엔진에 의해 브라우저에서 실행됨
- 실행 환경
  - HTML script 태그
  - js 확장자 파일
  - 브라우저 Console

<br/>

## DOM
- 웹 페이지(Document)를 구조화된 객체로 제공하며 프로그래밍 언어가 웹 페이지를 사용할 수 있게 연결

<br/>

### DOM 기본 개념
- 브라우저가 웹 페이지를 불러오는 과정
  - 문서(Document)는 웹 브라우저를 통해 해석되어 화면에 나타남
  - DOM은 이러한 문서를 조작하는 방법을 제공하는 API
- 브라우저는 HTML문서를 해석하여 DOM tree라는 객체의 트리로 구조화
- DOM에서 모든 요소, 속성, 텍스트는 하나의 객체이며 모두 Document객체의 자식
- 웹 페이지를 동적으로 만드는 것 = 웹 페이지를 조작하는 것
- 'document' object
  - 웹 페이지 객체
  - DOM Tree의 진입점
  - 페이지를 구성하는 모든 객체 요소를 포함
- 'document' 객체 접근 예시
  - HTML의 title 값을 변경하기

<br/>

### DOM Query (선택)
- 요소 하나 선택
  - document.querySelector()
    - 제공한 선택자와 일치하는 element 한 개 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null)
- 요소 여러 개 선택
  - document.querySelectorAll()
    - 제공한 선택자와 일치하는 여러 element를 선택
    - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음


<br/>

### DOM Manipulation (조작)
- 클래스 속성 조작
  - 'classList' property
    - 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
    - add()와 remove() 메서드를 사용해 지정한 클래스 값을 추가 혹은 제거
- classList 메서드 정리
  - element.classList.add()
    - 지정한 클래스 값을 추가
  - element.classList.remove()
    - 지정한 클래스 값을 제거
- 일반적인 속성 조작
  - 조회 .getAttribute()
  - 설정 .setAttribute()
  - 삭제 removeAttribute()
- 속성 조작 메서드 정리
  - Element.getAttribute()
    - 해당 요소에 지정된 값을 반환
  - Element.setAttribute()
    - 지정된 요소의 속성 값을 설정
    - 속성이 이미 있으면 값이 업데이트 / 그렇지 않으면 지정된 이름과 값으로 새 속성이 추가
  - Element.removeAttribute()
    - 요소에서 지정된 이름을 가진 속성 제거
- 'textContent' property
  - 요소의 텍스트 콘텐츠를 표현
- DOM 요소 조작
  - 생성
    - .createElement()
  - 추가
    - .appendChild()
  - 삭제
    - .removeChild()
- 'style' property
  - 해당 요소의 모든 스타일 속성 목록을 포함하는 속성

<br/>

### 종합 정리
1. 속성(attribute) 조작
  - 클래스 속성 조작
    - classList
    - add()
    - remove()
  - 일반 속성 조작
    - getAttribute()
    - setAttribute()
    - removeAttribute()
2. HTML 콘텐츠 조작
  - textContent
3. DOM 조작
  - createElement()
  - appendChild()
  - removeChild()
4. style 조작

### 예제 코드
- ex 1 / select
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1 class="title heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="text">content1</p>
  <p class="text">content2</p>
  <p class="text">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>

  <script>
    // console.log('hello')
    // 클래스가 title인 요소 선택
    console.log(document.querySelector('.title'))
    console.log(document.querySelector('.text'))
    console.log(document.querySelectorAll('.text'))
    console.log(document.querySelectorAll('ul > li'))
    
  </script>
</body>
</html>
```

- ex 2 / element manipulation
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1 class="title heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="text">content1</p>
  <p class="text">content2</p>
  <p class="text">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>

  <script>
    // 속성 조작
    // 클래스 속성 조작
    console.log(document.querySelector('h1'))
    const h1Tag = document.querySelector('h1')
    console.log(h1Tag.classList)

    h1Tag.classList.add('test')
    console.log(h1Tag.classList)

    h1Tag.classList.remove('test')
    console.log(h1Tag.classList)

    // 일반 속성 조작
    const aTag = document.querySelector('a')
    console.log(aTag)
    console.log(aTag.getAttribute('href'))

    aTag.setAttribute('href','https://www.naver.com/')
    console.log(aTag.getAttribute('href'))

    aTag.removeAttribute('href')
    console.log(aTag.getAttribute('href'))

    // 클래스도 일반 속성 방식으로 조작 가능
    const pTag = document.querySelector('.text')
    console.log(pTag.getAttribute('class'))
    
  </script>
</body>
</html>
```

- ex 3 / contents manipulation
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1 class="title heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="text">content1</p>
  <p class="text">content2</p>
  <p class="text">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>

  <script>
    // h1 tag 선택
    const h1Tag = document.querySelector('.heading')
    console.log(h1Tag.textContent)

    h1Tag.textContent = '콘텐츠 수정'
    console.log(h1Tag.textContent)
  </script>
</body>
</html>
```

- ex 4 / dom
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div></div>
  <script>
    // 1. 생성
    console.log(document.createElement('h1'))
    const h1Tag = document.createElement('h1')
    h1Tag.textContent = '제목'
    console.log(h1Tag)

    // 2. 추가
    // 추가할 부모를 선택
    const divTag = document.querySelector('div')
    divTag.appendChild(h1Tag)

    // 3. 삭제
    divTag.removeChild(h1Tag)

  </script>
</body>
</html>
```

- ex 5 / style
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>Heading</p>

  <script>
    const pTag = document.querySelector('p')

    pTag.style.color = 'red'
    pTag.style.fontSize = '3rem'

    console.log(pTag.style)

  </script>
</body>
</html>
```