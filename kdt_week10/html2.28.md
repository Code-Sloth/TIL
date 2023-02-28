# Web - Floating for CSS layout

<br/>

## CSS Float
- 요소를 띄워서 텍스트 및 인라인 요소가 그 주위를 감싸도록 하는 배치
  - 왼쪽 혹은 오른쪽으로 띄워 Normal Flow에서 벗어남

<br/>

### Float
- Float는 원래 탄생 목적에서 더 나아가 웹 페이지 전체 레이아웃을 구성하는 데 사용되었으나, Flexbox와 Grid의 등장으로 인해 다시 원래의 목적으로 돌아감

<br/>

## CSS Flexbox
- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
  - 요소 간 공간 배열과 정렬
- 기본 방향
  - 좌->우 / 상->하 , 축은 바뀔 수 있음에 유의
- main axis(주 축)
  - flex item들이 배치되는 기본 축
  - main start(좌상)에서 시작하여 main end(우상)방향으로 배치
- cross axis(교차 축)
  - main axis에 수직인 축
  - cross start(좌상)에서 시작하여 cross end(좌하)방향으로 배치
- Flex Container
  - display: flex; 혹은 display: inline-flex;가 설정된 부모 요소
  - 이 컨테이너의 1차 자식 요소들이 Flex item이 됨
  - flexbox 속성 값들을 사용하여 자식 요소 Flex item들을 배치

<br/>

### Flexbox 속성
- Flex Container 관련 속성
  - display, flex-direction, flex-wrap, justify-content, align-items, align-content
- Flex Item 관련 속성
  - align-self, flex-grow, flex-shrink, flex-basis, order

<br/>

### Flex 지정
- flex container
  - flex item은 행으로 나열
  - 주축의 시작 선에서 시작
  - 교차축의 크기를 채우기 위해 늘어남
  - display: flex;
- flex direction
  - flex item이 나열되는 방향을 지정
  - column으로 지정할 경우 주 축이 변경
  - reverse로 지정하면 시작 선과 끝 선이 서로 바뀜
  - row / column / row-reverse / column-reverse
- flex wrap
  - flex item 목록이 flex container의 하나의 행에 들어가지 않을 경우 다른 행에 배치할지 여부 설정
  - 개행 여부
  - wrap / nowrap
- justify content
  - 주 축을 따라 flex item과 주위에 공간을 분배
  - flex-start / center / flex-end / space-between / space-around / space-evenly
- align content
  - 교차 축을 따라 flex item과 주위에 공간을 분배
  - flex-wrap이 wrap또는 wrap-reverse로 설정된 여러 행에만 적용됨
  - 한 줄 짜리 행에는 (flex-wrap: nowrap;) 효과 없음
  - flex-start / center / flex-end / space-between / space-around / space-evenly
- align items
  - 교차 축을 따라 flex item 행을 정렬
  - flex-start / center / flex-end / stretch
- align self
  - 교차 축을 따라 개별 flex item을 정렬
  - flex-start / center / flex-end / stretch
- flex grow
  - 남는 행 여백을 비율에 따라 각 flex item에 분배
  - flex-grow의 반대는 flex-shrink
    - 넘치는 너비를 분배해서 줄임
  - 남는 픽셀이 200px이고 1,1,0,2가 있으면 50px 기준으로 50,50,0,100px를 분배
- flex basis
  - flex item의 초기 크기 값을 지정
  - flex-basis와 width값을 동시에 적용한 경우 flex-basis가 우선


<br/>

### 속성명 Tip
- justify : 주축
- align : 교차 축
- ~~-content : 여러 행
- ~~-items : 한 행
- ~~-self : 한 요소

<br/>

## 반응형 레이아웃
- flex-wrap을 사용해 반응형 레이아웃 작성 (flex-grow & flex-basis)


<br/>

## 참고
- justify-items 및 justify-self 속성이 없는 이유
  - margin auto를 통해 정렬 및 배치가 가능하기 때문에 필요가 없음
- shorthand 
  - flex-flow: flex-direction flex-wrap;
  - flex:
    - 숫자 : flex-grow
    - 길이&퍼센트 : flex-basis
    - 숫자 길이&퍼센트 : flex-grow flex-basis
    - 숫자 숫자 : flex-grow flex-shrink
    - 숫자 숫자 길이&퍼센트 : flex-grow flex-shrink flex-basis


<br/>

### 예제 코드
- ex 1) float
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
      width: 10rem;
      height: 10rem;
      border: 1px solid black;
      background-color: lightcoral;
    }


    .float-left {
      float: left;
    }

    .float-right {
      float: right;
    }
  </style>
</head>

<body>
  <div>
    <div class="box float-left">float left</div>
    <div class="box float-left">float left</div>
    <!-- <div class="box">div</div> -->
    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quia maxime dolore laboriosam atque non sequi, eum,
      odit, minus itaque quibusdam minima a reiciendis placeat nemo perspiciatis? Natus ipsam blanditiis, quos rem
      soluta nam quas esse repellendus illum a eum iure sed iste ex deleniti explicabo consectetur sit, debitis culpa
      officia unde? Qui eligendi distinctio suscipit cum quos excepturi deleniti non assumenda dicta dolorum delectus
      saepe porro, asperiores harum repellat quia voluptates incidunt itaque doloremque, expedita quam tempora
      veritatis! Tempore laborum fuga totam cum! Repudiandae, quisquam adipisci excepturi, voluptates non omnis ratione
      placeat inventore ab laudantium modi porro. Culpa eos enim voluptas deleniti quis suscipit ipsam eaque. Maiores
      vitae ipsa, excepturi repudiandae quia aut culpa laborum mollitia magni earum optio labore est! Eveniet expedita
      architecto excepturi hic iusto? At modi adipisci tenetur sed quod, unde corrupti animi iste, perferendis
      voluptatibus odio quis ea id itaque architecto voluptate laudantium inventore quasi est necessitatibus vel
      voluptates dolores. Vero perspiciatis consectetur aspernatur tempore nobis porro, fugit cum tenetur repellat harum
      sed quae laborum quos dolorum quaerat incidunt optio dicta voluptate voluptatem nihil. Nostrum, impedit quae earum
      illo ut veniam molestias? Mollitia nisi eum doloribus laboriosam ducimus deleniti voluptate porro corrupti nostrum
      ab, alias necessitatibus?</p>
    <div class="box float-right">float right</div>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis explicabo provident recusandae quibusdam ipsam rem
      impedit reprehenderit fugiat quod maiores excepturi eius perferendis est perspiciatis natus magnam quasi culpa a
      magni aut, expedita, dolorem sed. Vel provident similique id quam nemo culpa saepe hic ipsum mollitia quod rerum
      adipisci, dolor voluptas commodi ex inventore in. Nesciunt autem expedita accusamus corporis ex doloribus
      voluptates quia, neque deleniti distinctio adipisci odit incidunt. Distinctio ipsum, velit temporibus nam nulla
      maiores nihil hic ducimus. Atque quidem repellat molestiae sint laboriosam voluptatum, in totam autem debitis
      libero non. Repellat hic sequi dolorum, beatae ratione sed magnam placeat quos itaque reiciendis pariatur cum
      recusandae enim sit amet veritatis delectus voluptatibus repudiandae, explicabo accusamus aliquam facilis sunt nam
      assumenda. Alias non laudantium quia perspiciatis debitis. Mollitia tempora praesentium, culpa molestiae, ab esse
      itaque saepe libero tempore nesciunt maiores, sapiente quas dignissimos dolorem aspernatur corporis veniam minima
      quod similique optio. Optio animi laborum amet nostrum et aperiam! Corporis, aliquam odio incidunt asperiores
      animi in unde quo. Tempora exercitationem, inventore quo commodi cumque veritatis. Iste, ea. Voluptates quis
      blanditiis perspiciatis vitae est possimus explicabo atque ex maiores dignissimos cumque animi laudantium,
      voluptate culpa minima, deleniti saepe eaque aperiam omnis.</p>
  </div>
</body>

</html>
```

- ex 2) flexbox
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      height: 500px;
      border: 1px solid black;
      display: flex;
      flex-direction: row; /*주축 : 좌우*/
      /* flex-direction: column; 주축 : 상하 */
      /* flex-direction: row-reverse; */

      /* flex-wrap: nowrap; */
      /* flex-wrap: wrap; */

      /* 주축 정렬 */
      /* justify-content: center;
      justify-content: flex-start;
      justify-content: flex-end; */

      /* 교차축 정렬 */
      /* align-content: flex-start;
      align-content: center;
      align-content: flex-end; */

      /* align-items: flex-start;
      align-items: center;
      align-items: flex-end; */
    }

    .post {
      background-color: grey;
      border: 1px solid black;
      margin: 0.5rem;
      padding: 0.5rem;
    }

    .item1 {
      align-self: center;
    }

    .item2 {
      align-self: flex-end;
    }

  </style>
</head>

<body>
  <div class="container">
    <div class="post item1">
      <h2>Post Title 1</h2>
      <p>Post Content 1</p>
    </div>
    <div class="post item2">
      <h2>Post Title 2</h2>
      <p>Post Content 2</p>
    </div>
    <div class="post">
      <h2>Post Title 3</h2>
      <p>Post Content 3</p>
    </div>
    <div class="post">
      <h2>Post Title 4</h2>
      <p>Post Content 4</p>
    </div>
  </div>

</body>

</html>
```

- ex 3) flexbox_grow
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      width: 100%;
      display: flex;
    }

    .item {
      height: 100px;
      color: white;
      font-size: 3rem;
    }

    .item-1 {
      background-color: red;
      flex-grow: 1;
    }

    .item-2 {
      background-color: green;
      flex-grow: 2;
    }

    .item-3 {
      background-color: blue;
      flex-grow: 3;
    }

  </style>
</head>

<body>
  <div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
  </div>
</body>

</html>
```

- ex 4) flexbox_basis
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      width: 100%;
      display: flex;
    }

    .item {
      height: 100px;
      color: white;
      font-size: 3rem;
    }

    .item-1 {
      background-color: red;
      flex-basis: 300px;
    }

    .item-2 {
      background-color: green;
      flex-basis: 400px;
    }

    .item-3 {
      background-color: blue;
      flex-basis: 200px;
    }

  </style>
</head>

<body>
  <div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
  </div>
</body>

</html>
```

- ex 5) flexbox_responsive
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .card {
      border: 1px solid black;
      width: 80%;
      display: flex;
      flex-wrap: wrap;
    }

    img {
      width: 100%;
    }

    .card-img {
      flex-basis: 700px;
      flex-grow: 1;
      flex: 1 700px;
    }

    .content {
      flex-basis: 110px;
      border: 1px solid blue;
      flex-grow: 1;
      flex: 1 110px;
    }

  </style>
</head>
<body>
  <div class="card">
    <img class="card-img" src="../html_practice2.27/01_이미지 위 이미지/01.jpg" alt="sample">
    <div class="content">
      <h2>Heading</h2>
      <p>.......</p>
    </div>
  </div>
</body>
</html>
```