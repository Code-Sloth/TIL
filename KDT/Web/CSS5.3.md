# CSS 참고

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