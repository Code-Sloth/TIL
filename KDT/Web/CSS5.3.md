# CSS 참고

<br/>

### Link
- ```css
    a:link {color: black;}
    a:visited {color: black;}
    a:hover {color: gray;}
    a:active {color: purple;}
  ```

<br/>

### Text 1줄
- ```css
    .single-line {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
  ```

<br/>

### Text 2줄
- ```css
    .multi-line {
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      /* 줄바꿈 */
      word-break: break-word;
    }
  ```

<br/>

### 자연스러운 변형 효과
- ```css
    .box {
      transition: transform 0.3s ease;
    }

    .box:hover {
      transform: scale(0.1)
    }
  ```

<br/>

### 박스 섀도우
- ```css
    .box {
      box-shadow: 1px 7px 15px 4px rgba(0,0,0,0.1);
      /* 오른쪽,아래쪽 */
      box-shadow: 0px 0px 0px 0px rgba(0,0,0,0.1), 5px 5px 15px 0px rgba(0,0,0,0.1);
    }
  ```

<br/>

### 간단한 애니메이션 효과
- ```css
    .box {
      width: 65px;
      height: 65px;
      animation: heartbeat 1.5s infinite;
    }

    @keyframes heartbeat {
      0% {
          transform: scale( .9 );
      }
      20% {
          transform: scale( 1 );
      }
      40% {
          transform: scale( .9 );
      }
      60% {
          transform: scale( 1 );
      }
      80% {
          transform: scale( .9 );
      }
      100% {
          transform: scale( .9 );
      }
    }
  ```

<br/>

### Image Hover Transform
- ```css
    .imgDiv {
      width: 269px;
      overflow: hidden;
    }

    .imgDiv img {
      border-radius: 10px;
      transition: transform 0.3s ease;
    }

    .imgDiv img:hover {
      transform: scale(1.05);
    }
  ```

<br/>

### 투명색
- ```css
    div {
      background-color: #fff0;
    }
  ```

<br/>

### input 우측 x표 제거
- ```css
    input::-webkit-search-cancel-button {
      display: none;
    }
  ```

<br/>

### input 입력 시, outline 제거
- ```css
    input:focus {
      outline: none;
    }
  ```

<br/>

### media query
- ```css
    @media(max-width: 1200px) {
      .comment-detail-container {
        margin-left: 0;
        width: 100%;
      }

      .comment-detail-left-header {
        width: 100%;
      }
    }

    @media(max-width: 1024px) {
      .comment-detail-right {
        display: none;
      }

      .detail-left-footer-box h2 div {
        font-size: 12px;
      }
    }
  ```

<br/>

### 가운데 .
- ```html
    <span>&nbsp;·&nbsp;</span>
  ```

<br/>

### 선택자
- ```css
    /* div1안에 div2가 있다 가정 */
    .div1:hover .div2 {
      background-color: red;
    }

    .div2:hover + .div1 {
      background-color: red;
    }

    /* div3요소 이후의 모든 div요소들을 지정 */
    .div3 ~ div {
      background-color: red;
    }

    /* ul 자식 중 첫 번째 요소 선택 */
    ul li:first-child {
      background-color: red;
    }

    /* ul 자식 중 마지막 요소 선택 */
    ul li:last-child {
      background-color: red;
    }

    /* disabled 제외 */
    .ul button:not(:disabled) {
      background-color: red;
    }

    /* class 여러 개 제외 */
    .ul li:not(.aaa):not(.bbb) {
      background-color: red;
    }
  ```

<br/>

### scale 줄였을 때 빈 공간 이동
- ```css
    div {
      transform: scale(0.8);
      transform-origin: top right;
    }
  ```

<br/>

### absolute 가운데 정렬
- ```css
    .owl-dots {
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
    }
  ```

