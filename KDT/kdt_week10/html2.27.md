# Web - Positioning for CSS layout

<br/>

### CSS Layout
- 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것

<br/>

## 포지션
- Normal Flow에서 요소를 끄집어내서 다른 위치로 배치하는 것
  - 다른 요소 위에 놓기, 화면 특정 위치에 고정시키기 등
  - Normal Flow : CSS를 적용하지 않았을 경우 웹페이지 요소가 기본적으로 배치되는 방향
- static
  - 기본값
  - 요소를 Normal Flow에 따라 배치
- relative
  - 요소를 Normal Flow에 따라 배치
  - 자기 자신을 기준으로 이동
  - 요소가 차지하는 공간은 static일 때와 같음
- absolute
  - 요소를 Normal Flow에서 제거
  - 가장 가까운 relative 부모 요소를 기준으로 이동
  - 문서에서 요소가 차지하는 공간이 없어짐
- fixed
  - 요소를 Normal Flow에서 제거
  - 현재 화면영역(viewport)을 기준으로 이동
  - 문서에서 요소가 차지하는 공간이 없어짐
- sticky
  - 요소를 Normal Flow에 따라 배치
  - 가장 가까운 block 부모 요소를 기준으로 이동
  - 요소가 특정 임계점에 스크롤될 때 그 위치에서 고정됨(fixed)
    - 이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치게 되기 때문
- z-index
  - 요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼 지 결정
  - 기본 z-index : 0
  - 더 큰 값을 가진 요소가 작은 값의 요소를 덮음

<br/>

### 포지션의 역할
- CSS Position은 전체 페이지에 대한 레이아웃을 구성하는 것이 아닌 페이지의 특정 항목의 위치를 조정하는 것에 관한 것

<br/>

### 예제 코드
- ex 1) position
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
      box-sizing: border-box;
    }

    body {
      height: 1500px;
    }

    .box {
      width: 100px;
      height: 100px;
      border: 1px solid black;
    }

    .container {
      width: 300px;
      height: 300px;
      border: 1px solid black;
      position: relative;
    }

    .static {
      position: static;
      background-color: lightcoral;
    }

    .absolute {
      position: absolute;
      background-color: lightgreen;
      left: 100px;
    }

    .relative {
      position: relative;
      background-color: lightblue;
      left: 100px;
      top: 100px;
    }

    .fixed {
      position: fixed;
      right: 0;
      top: 0;
      background-color: gray;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="box static">static</div>
    <div class="box absolute">absolute</div>
    <div class="box relative">relative</div>
    <div class="box fixed">fixed</div>
  </div>
</body>
</html>
```

- ex 2) sticky
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    body {
      height: 1500px;
    }

    .sticky {
      position: sticky;
      background-color: lightblue;
      border: 1px solid black;
      top: 0px;
    }

  </style>
</head>
<body>
  <div>
    <div class="sticky">sticky</div>
    <div>
      <p>aa</p>
      <p>aa</p>
      <p>aa</p>
    </div>
    <div class="sticky">sticky</div>
    <div>
      <p>aa</p>
      <p>aa</p>
      <p>aa</p>
    </div>
    <div class="sticky">sticky</div>
    <div>
      <p>aa</p>
      <p>aa</p>
      <p>aa</p>
    </div>
  </div>
</body>
</html>
```

- ex 3) z-index
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
      height: 100px;
      position: absolute;
    }

    .red {
      background-color: red;
      top: 75px;
      left: 75px;
      z-index: 3;
    }

    .blue {
      background-color: blue;
      top: 100px;
      left: 100px;
      /* z-index: 2; */
    }

    .green {
      background-color: green;
      top: 150px;
      left: 150px;
      z-index: -1;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="box red"></div>
    <div class="box blue"></div>
    <div class="box green"></div>
  </div>
</body>
</html>
```

- ex 4) absolute
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
      box-sizing: border-box;
    }

    .container {
      position: relative;
      border: 1px solid black;
    }

    .link {
      width: 10px;
      height: 10px;
      background-color: black;
      text-align: center;
      line-height: 10px;
      border-radius: 50%;
      text-decoration: none;
      font-size: 10%;
    }

    .link-position {
      position: absolute;
      left: 0;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
    }

    .img {
      width: 100%;
    }

  </style>
</head>
<body>
  <div class="container">
    <img src="bespoke.jpg" alt="#" class="img">
    <a href="#" class="link link-position">비교하기</a>
  </div>
</body>
</html>
```