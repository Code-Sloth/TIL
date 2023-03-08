# Web - Grid system for responsive web design

<br/>

## Responsive Web Design
- 디바이스 종류나 화면 크기에 상관없이, 어디에서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술
- Bootstrap grid system의 12개의 column과 6개의 breakpoints를 사용하여 반응형 웹 디자인을 구현

<br/>

### Grid system breakpoints
- 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
- xs <576px
- sm >=576px
- md >=768px
- lg >=992px
- xl >=1200px
- xxl >=1400px

<br/>

### summery
- 각각의 기술은 용도와 장단점이 존재
- 어떤 기술도 독립적인 용도를 가지지 않으며, 어떤 기술이 적합한 도구가 될지는 특정 상황에 따라 다름
- 이를 파악하기 위해서는 충분한 경험이 필요

<br/>

### 참고
- Grid cards
  - row-cols 클래스를 사용하여 행당 표시할 열 수를 손쉽게 제어 가능
  - row row-cols4 row-cols-lg-2

<br/>

## UX & UI

<br/>

### UX (User Experience)
- 제품이나 서비스를 사용하는 사람들이 느끼는 전체적인 경험과 만족도를 개선하고 최적화하기 위한 디자인과 개발 분야
- 예시
  - 백화점 1층에서 느껴지는 좋은 향수 향기
  - 러쉬 매장 근처만 가도 맡을 수 있는 러쉬 향기
  - 원하는 음악을 검색할 때, 검색 기능이 적절하게 작동하고 검색 결과가 정확하게 나오는 것
- 설계
  - 사람들의 마음과 생각을 이해하고 정리해서 제품에 녹여내는 과정이 필요
  - 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 등이 필요

<br/>

### UI (User Interface)
- 서비스와 사용자 간의 상호작용을 가능하게 하는 디자인 요소들을 개발하고 구현하는 분야
- 예시
  - 리모콘
  - ATM
  - 웹 사이트
- 설계
  - 예쁜 디자인보다는 사용자가 더 쉽고 편리하게 사용할 수 있도록 고려
  - 이를 위해서는 디자인 시스템, 중간 산출물, 프로토 타입 등이 필요

<br/>

## UX & UI 직무
- UX
  - 구글 : 사용자의 경험을 이해하기 위한 통계 모델을 설계
    - https://developer.apple.com/kr/design/tips/
  - MS : 리서치를 기획하고 사용자에 대한 지표를 정의
  - Meta : 정성적인 방법과 정량적인 방법을 사용하여 사용자 조사를 실시
- UI
  - 구글 : 다양한 디자인 프로토타이핑 툴을 사용해 개발 가이드를 제공
  - MS : 시각 디자인을 고려해서 체계적인 디자인 컨셉을 보여줌
  - Meta : 제품을 이해하고 더 나은 UI Flow와 사용자 경험을 디자인


### 예제 코드
- ex 1 / breakpoints
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
  <style>
    .box {
      border: 1px solid black;
      background-color: lightblue;
      text-align: center;
    }
  </style>
</head>
<body>
  
  <div class="container">
    <h2>Breakpoint</h2>
    <div class="row gx-0">
      <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>

      <div class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>

      <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        <div class="box">col</div>
      </div>

      <div class="col-12 col-sm-6 col-md-12 col-lg-3 col-xl-12">
        <div class="box">col</div>
      </div>

      <h2>breakpoints + offset</h2>
      <div class="row">
        <div class="col-12 col-sm-4 col-md-6">
          <div class="box">col</div>
        </div>

        <div class="col-12 col-sm-4 col-md-6">
          <div class="box">col</div>
        </div>

        <div class="col-12 col-sm-4 col-md-6">
          <div class="box">col</div>
        </div>

        <div class="col-12 col-sm-4 offset-sm-4 col-md-6 offset-md-0">
          <div class="box">col</div>
        </div>
      </div>
    </div>
  </div>


  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
</html>

```

- ex 2 / grid cards.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
</head>
<body>

  <div class="container">

    <div class="row row-cols-1 row-cols-md-2 g-4">
      <div class="col">
        <div class="card">
          <img src="..." class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="..." class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="..." class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img src="..." class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
</html>

```