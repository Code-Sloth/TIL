# 자바스크립트 개념

<br/>

### 동작 원리
- 브라우저에 내장되어있는 자바스크립트 엔진의 런타임시 코드를 한줄씩 번역해서 실행(interpreter)
  - 초반 실행속도는 빠르지만 비교적 느림
- 다른 언어는 compiler / 코드 => Compiler => 실행파일 => 실행
  - 컴파일링 단계에서 시간이 오래 걸리지만 만들어둔 실행파일로 인해 실행속도가 빠름

<br/>

### 엔진
- Internet Exporer
  - Chakra
- Edge Browser
  - V8
- Google Chrome
  - V8
- Safari
  - JavaScript Core
- Firefox
  - SpiderMonkey
- Node.js
  - V8

<br/>

### ECMAScript
- JavaScript 문법의 규격사항, 표준사항
- JS => ECMAScript => 엔진
- [History](https://en.wikipedia.org/wiki/ECMAScript)
  - 2015년 ES6(큰 변화)
- [버전별 문법 지원 현황](https://kangax.github.io/compat-table/es5/)

<br/>

### 특징
- 가볍고, Interpreter로 한 줄씩 번역, 1급 함수를 가짐
- 브라우저가 아닌 환경에서도 사용 가능(자바스크립트 엔진이 있는 곳)
- Prototype-based, multi-paradigm, single-threaded, dynamic language

<br/>

### 공부 방법
- 프로그래밍 언어
  - 개발자는 `정해진 문법`으로 특정한 로직을 수행하도록 프로그래밍 함
- 언어 => 출력(외부환경 / 라이브러리)
- 언어 => 통신(외부환경 / 라이브러리)
- Browser
  - Front-end(Vue, React, Angular)
    - WebAPIs
      - DOM APIs
      - Network APIs
      - Storage APIs
  - Back-end(Express, Nest)
    - Node.js API
      - console
      - crypto
      - HTTP
      - file
      - OS
- JavaScript 언어를 공부하고 나서 여러 API 사용

<br/>

### JavaScript 구성
- Basic(기본문법, 사용법)
  - let, const
  - if, for, switch, while
  - function
  - object
- Advanced(내부 구현사항)
  - Prototype
    - Hoisting
  - Scope
    - Closure
