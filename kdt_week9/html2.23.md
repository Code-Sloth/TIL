# Web - The Box Model

<br/>

## CSS Box Model
- 모든 HTML 요소를 (사각형) 박스로 표현
- 박스에 대한 크기 여백 테두리 등의 스타일을 지정하는 디자인 개념

<br/>

### Box 구성
![box1](https://raw.githubusercontent.com/Code-Sloth/TIL/master/kdt_week9/box1.png)
- Margin : 이 박스와 다른 박스 요소 사이의 공백/ 가장 바깥쪽 영역
- Border : 콘텐츠와 패딩을 감싸는 테두리 영역
- Padding : 콘텐츠 주위에 위치하는 공백 영역
  - Padding의 왼쪽 값을 키운다 => 컨텐츠가 오른쪽으로 간다
- Content : 콘텐츠가 표시되는 영역

<br/>

### box-sizing 속성
- width & height는 콘텐츠 영역을 대상
- box-sizing으로 요소의 너비와 높이를 계산하는 방법을 지정
  - box-sizing: content-box;
  - box-sizing: border-box;

<br/>

## Box 타입
- block 타입
  - display: block;
  - 항상 새로운 행으로 나뉨
  - width와 height 속성을 사용하여 너비와 높이를 지정 가능
  - 기본적으로 width 속성을 지정하지 않으면 박스는 inline방향으로 사용 가능한 공간을 모두 차지(너비를 사용가능한 공간의 100%로 채움)
  - 대표적인 block타입 태그
    - h1~6, p, div
- inline 타입
  - display: inline;
  - 새로운 행으로 나뉘지 않음
  - width와 height 속성을 사용할 수 없음
  - 수직 방향
    - padding, margins, borders가 적용되지만 밀어내지는 못함
  - 수평 방향
    - padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음
  - 대표적인 inline 타입 태그
    - a, img, span

<br/>

## 참고

<br/>

### shorthand 속성 - border
- border-width, border-style, border-color를 한번에 설정 가능 (순서 상관 x)
  - border: 1px solid black;
- 4방향
  - 4개 => 상 우 하 좌
  - 3개 => 상 (좌우) 하
  - 2개 => (상하) (좌우)
  - 1개 => 공통

<br/>

### display: inline-block
- inline과 block요소 사이의 중간 지점을 제공하는 display값
- 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용
- block요소의 특징을 가짐
  - 너비 및 높이 속성이 준수
  - 패딩, 여백 및 테두리로 인해 다른 요소가 상자에서 밀려남

<br/>

### 마진 상쇄(Margin collapsing)
- 두 block 타입 요소의 margin top과 bottom이 만나 큰 margin으로 결합
- 웹 개발자가 레이아웃을 더욱 쉽게 관리 가능

<br/>

### 예제 코드
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box1 {
      border-style: solid;
      border-width: 3px;
      border-color: red;
      border-bottom-color: blue;
      margin-top: 50px;
      margin-left: 30px;
      width: 300px;
      padding-left: 50px;
    }

    .box2 {
      width: 300px;
      border: 1px solid black; /* shorthand 작성 순서 무관*/
      margin: 25px auto; /*25px : 상하 auto : 좌우*/
    }

    .box3 {
      width: 300px;
      border: 1px solid black;
      margin-left: auto; /* 기본 : margin-right: auto; 오른쪽 마진을 왼쪽으로 모두 보낸다 */
    }
  </style>
</head>
<body>
  <div class="box1">box1</div>
  <div class="box2">box2</div>
  <div class="box3">box3</div>
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
    .box {
      width: 100px;
      border: 2px solid black;
      background-color: gray;
      margin: 20px;
      padding: 25px;
    }
    .content-box {
      box-sizing: content-box;
    }

    .border-box {
      box-sizing: border-box;
    }
  </style>
</head>
<body>
  <div class="box content-box">content-box</div>
  <div class="box border-box">border-box</div>
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
    a,
    span,
    img {
      border: 1px solid red;
      padding-top: 50px;
      padding-right: 50px;
    }

    h1,
    p,
    div {
      border: 1px solid blue;
    }

  </style>
</head>
<body>
  <h1>Normal Flow</h1>
  <p>p태그도 대표적인 block 요소</p>
  <div>
    <p>block요소는 기본적으로 부모 요소 너비의 100%를 차지하며, 높이는 자식콘텐츠의 최대 높이를 취한다.</p>
    <p>block 요소의 총 너비와 총 높이는 content + padding + border(상하/좌우 두께)</p>
    <p>block 요소는 서로 margins로 구분된다.</p>
    <p>inline 요소는 <span>이 span 태그처럼</span> 자기 콘텐츠의 너비와 높이만 차지한다.
    그리고 inline 요소는 <a href="">width나 height 속성을 지정할 수 없다.</a>
    </p>
    <p>
      이미지 <img src="#" alt="#"> 또한 inline 요소 중 하나이다.<br/>
      단, 이미지는 다른 inline 요소들과 달리 width나 height값을 지정할 수 있다.
    </p>
    <p>
      만약 inline 요소의 크기를 제어하려면 block으로 변경해버리거나 inline-block 요소로 설정해주어야 한다.
    </p>
  </div>
</body>
</html>
```