# 참조 자료형

<br/>

## Function
- 참조 자료형에 속하며 모든 함수는 Function object
- 함수의 이름
- 함수의 매개변수
- 함수의 body를 구성하는 statement
- 선언식
  - funtion funcName() {statements}
- 표현식
  - const funcName = function() {statements}
  - 함수 이름이 없는 익명 함수를 사용할 수 있음
  - 선언식과 달리 표현식으로 정의한 함수는 호이스팅 되지 않으므로 코드에서 나타나기 전에 먼저 사용할 수 없음
  - 사용 권장

### 기본 함수 매개변수
- 값이 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화
- 매개변수와 인자의 개수 불일치
  - 매개변수 개수 < 인자 개수 : 매개변수 개수만큼 나옴
  - 매개변수 개수 > 인자 개수 : 더 많은 인자의 출력은 undefined
- 나머지 매개변수
  - 무한한 수의 인자를 배열로 허용하여 가변 함수를 나타내는 방법

<br/>

### 화살표 함수 표현식
- 함수 표현식의 간결한 표현법
  1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>) 작성
  2. 함수의 매개변수가 하나 뿐이라면 매개변수의 () 제거 가능
  3. 함수 본문의 표현식이 한 줄이라면 {}와 return 제거 가능

<br/>

### 참고
- 인자가 없다면 () or _ 로 표시 가능
- object를 return한다면 return을 명시적으로 작성해야 함
- return을 적지 않으려면 ()로 감싸야 함

<br/>

## Object
- 키로 구분된 데이터 집합(data collection)을 저장하는 자료형
- 객체의 구조
  - 중괄호를 이용해 작성
  - 중괄호 안에는 key:value 쌍으로 구성된 속성(property)를 여러 개 넣을 수 있음
  - key는 문자형, value는 모든 자료형이 허용
- trailing comma(마지막 요소에 ,) : 속성을 추가, 삭제, 이동하기가 용이

<br/>

### 객체의 속성
- Property 존재 여부 확인 in
- 단축 Property
  - 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음
- 계산된 Property
  - 키가 대괄호[]로 둘러싸여 있는 property
  - 고정된 값이 아닌 변수 값을 사용할 수 있음

<br/>

### 객체와 함수
- Method
  - 객체 속성에 정의된 함수
  - object.method() 메서드는 객체를 행동할 수 있게 함
  - this 키워드를 사용해 객체에 대한 특정한 작업을 수행 할 수 있음
- this keyword
  - 함수나 메서드를 호출한 객체를 가리키는 키워드
  - 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용
  - 단순 호출 시 => 전역 객체
  - 메서드 호출 시 => 메서드를 호출한 객체
- Nested함수에서의 this
  - forEach의 인자로 들어간 함수는 일반 함수 호출이기 때문에 전역 객체를 가리킴
  - 화살표 함수는 자신만의 this를 가지지 않기 때문에 외부 함수에서 this 값을 가져옴
  - 따라서 메서드 정의 할 때는 화살표 함수 금지

<br/>

### 참고
- 유용한 객체 메서드
  - Object.keys(func_name)
  - Object.values(func_name)
- JavaScript this 특징
  - 함수가 호출되는 방식에 따라 결정되는 현재 객체를 나타냄
  - Python의 self와 Java의 this는 선언 시 값이 이미 정해지는 것에 비해 JavaScript의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨(동적)
- JSON (JavaScript Object Notation)
  - Key-Value 형태로 이루어진 자료 표기법
  - JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 문자열
  - JavaScript에서 JSON을 사용하기 위해서는 Object자료형으로 변경해야 함
- JSON => Object
  - const objToJson = JSON.stringify(jsObject)
- Object => JSON
  - const jsonToObj = JSON.parse(objToJson)

<br/>

## Array
- 순서가 있는 데이터 집합(data collection)을 저장하는 자료구조
- 배열의 구조
  - 대괄호를 이용해 작성
  - length를 사용해 배열에 담긴 요소가 몇 개인지 알 수 있음
  - 배열 요소의 자료형엔 제약이 없음
  - 배열의 마지막 요소는 객체와 마찬가지로 쉼표로 끝날 수 있음(trailing comma)

<br/>

### 배열과 메서드
- push / pop
  - 배열 끝 요소를 추가 또는 제거
- unshift / shift
  - 배열 앞 요소를 추가 또는 제거
- forEach
  - 인자로 주어진 함수(콜백함수)를 배열 요소 각각에 대해 실행 / 반복
  - ```JavaScript
      array.forEach(function (item,index,array)) {
        // do something
      }
      콜백함수는 3가지 매개변수로 구성
      item: 배열의 요소
      index: 배열 요소의 인덱스
      array: 배열
      반환 값: undefined
    ``` 
- 콜백 함수
  - 다른 함수에 인자로 전달되는 함수
  - 외부 함수내에서 호출되어 일종의 루틴이나 특정 작업을 진행
- map
  - 배열 요소 전체를 대상으로 함수(콜백함수)를 호출하고, 함수 호출 결과를 배열로 반환 / 변형

<br/>

### 배열 정리
- 배열의 본질은 객체
- 배열의 요소를 대괄호 접근법을 사용해 접근하는 건 객체 문법과 같음
- 다만 배열의 키는 숫자라는 점
- 숫자형 키를 사용함으로써 배열은 객체 기본 기능 이외에도 순서가 있는 컬렉션을 제어하게 해주는 특별한 메서드를 제공

<br/>

### 참고
- 배열 순회 종합
  - for loop
    - 배열의 인덱스를 이용하여 각 요소에 접근
  - for...of
    - 배열 요소에 바로 접근 가능
  - forEach
    - 간결하고 가독성이 높음
    - callback함수를 이용하여 각 요소를 조작하기 용이
    - break, continue 사용 불가능
    - 사용 권장
- 콜백함수 구조를 사용하는 이유
  - 함수의 재사용성 측면
    - 함수를 호출하는 코드에서 콜백 함수의 동작을 자유롭게 변경 가능
    - 예를 들어, map함수는 콜백 함수를 인자로 받아 배열의 각 요소를 순회하며 콜백 함수를 실행
    - 이 때, 콜백 함수는 각 요소를 변환하는 로직을 담당하므로, map함수를 호출하는 코드는 간결하고 가독성이 높아짐
  - 비동기적 처리 측면
    - ```JavaScript
        console.log('a')

        setTimeout(() => {
          console.log('b')
        }, 3000)

        console.log('c')
        
        출력 결과 : a c b
        setTimeout 함수는 콜백 함수를 인자로 받아 일정 시간이 지난 후에 실행됨
        이 때, setTimeout 함수는 비동기적으로 콜백 함수를 실행하므로, 다른 코드의 실행을 방해하지 않음
      ```

<br/>

### 예제 코드
- ex 1 / function
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
  <script>
    // 함수 선언식
    function add (num1, num2) {
      return num1 + num2
    }

    console.log(add(3, 9))
    
    // 함수 표현식
    const sub = function (num1, num2) {
      return num1 - num2
    }

    console.log(sub(3, 9))

    // 기본 함수 매개변수
    const greeting = function (name = 'Anonymous') {
      return `Hi ${name}`
    }

    console.log(greeting())

    // 매개변수 개수와 인자 개수의 불일치 상황
    // 매개변수 개수 < 인자
    const noArgs = function () {
      return 0
    }

    console.log(noArgs(1,2,3))

    const twoArgs = function (num1,num2) {
      return [num1,num2]
    }

    console.log(twoArgs(1,2,3))

    // 매개변수 개수 > 인자
    const threeArg = function (num1,num2,num3) {
      return [num1,num2,num3]
    }

    console.log(threeArg(1))

    // 나머지 매개변수
    const myFunc = function (num1,num2,...restArgs) {
      return [num1,num2,restArgs]
    }

    console.log(myFunc(1,2,3,4,5))
    console.log(myFunc(1,2))
  </script>
</body>
</html>
```

- ex 2 / arrow
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
  <script>
    const greeting = function (name) {
      return `hello, ${name}`
    }

    const arrow1 = (name) => {
      return `hello, ${name}`
    }

    // 보통 여기까지만 쓰임

    console.log(arrow1('harry'))

    const arrow2 = (name) => `hello, ${name}`

    console.log(arrow2('harry'))
  </script>
</body>
</html>
```

- ex 3 / object
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
  <script>
    const user = {
      name: 'Sophia',
      age: 30,
      'key with space': true,
    }

    // 조회
    console.log(user.age)
    console.log(user['age'])
    console.log(user['key with space'])

    // 추가
    user.address = 'korea'
    console.log(user.address)

    // 수정
    user.age = 40
    console.log(user.age)

    // 삭제
    delete user.address
    console.log(user)

    // in 연산자
    console.log('age' in user)
    console.log('country' in user)

    // 단축 속성
    const age = 30
    const address = 'korea'

    const oldUser = {
      age: age,
      address: address,
    }

    const newUser = {
      age,
      address,
    }

    // 계산된 속성
    const product = prompt('물건 이름을 입력해주세요.')
    const a = 'my'
    const b = 'property'

    const bag = {
      [product]: 5,
      [a + b]: true,
    }

    console.log(bag)

    
  </script>
</body>
</html>
```

- ex 4 / method
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
  <script>
    const person = {
      name: 'Sophia',
      greeting: function () {
        return `hello, my name is ${this.name}`
      },
    }

    // greeting 메서드 호출
    console.log(person.greeting())

    // this
    // 단순 호출 시
    const myFunc = function () {
      return this
    }

    console.log(myFunc())

    // nested 함수에서의 this
    const myObj2 = {
      numbers: [1,2,3],

      myFunc: function () {
        this.numbers.forEach(function (number) {
          console.log(number)
          console.log(this)
        })
      }
    }
    console.log(myObj2.myFunc())


    // nested 함수에서의 this 화살표 함수
    const myObj3 = {
      numbers: [1,2,3],

      myFunc: function () {
        this.numbers.forEach((number) => {
          console.log(number)
          console.log(this)
        })
      }
    }
    console.log(myObj3.myFunc())

  </script>
</body>
</html>
```

- ex 5 / forEach
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
  <script>
    const fruits = ['apple','banana','coconut']

    // forEach
    fruits.forEach(function (fruit,idx) {
      console.log(fruit,idx)
    })

    // map
    const numbers = [1,2,3]

    const callbackFunc = function (number) {
      return number * 2
    }

    const doubleNumbers1 = numbers.map(callbackFunc)

    const doubleNumbers2 = numbers.map(function (number) {
      return number * 2
    })

    console.log(doubleNumbers1)
    console.log(doubleNumbers2)

    console.log('a')

    setTimeout(() => {
      console.log('b')
    }, 3000)

    console.log('c')
  </script>
</body>
</html>
```
