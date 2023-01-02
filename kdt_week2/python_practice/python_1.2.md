# Python 기초

<br/>

## 컴퓨터 프로그래밍 언어

<br/>

### **`컴퓨터`** 
- Caculaion (조작)
- Remember (저장)

<br/>

### **`프로그래밍`**
- 명령어의 모음 (집합)

<br/>

### **`언어`**
- 자신의 생각을 나타내고 전달하기 위해 사용하는 체계
- 문법적으로 맞는 말의 집합

<br/>

### **`지식`**
- 선언적 지식(declarative knowledge)
  - 사실에 대한 내용 ex) 삼성은 1등이다.
- 명령적 지식(imperative knowledge)
  - 어떻게 ex) 일본에 가는 법은?

<br/>

## 파이썬

<br/>

- 배우기 쉽다
  - 문법이 간단, 엄격하지 않음
    - ex) 변수에 별도의 타입 지정 x
  - 문법 표현이 간결, 배우는 데 짧은 시간 소요
    - ex) 문장을 구분할때 {}대신 들여쓰기 사용
- Expressive Language
  - 같은 작업을 해도 다른 언어보다 간결
- 크로스 플랫폼 언어
  - 다양한 운영체제에서 실행 가능
- 특징
  - 인터프리터 언어 (interpreter)
    - 컴파일 과정 없이 실행 가능
    - 간결하게 입력하고 실행한 후 바로 확인 가능
  - 객체 지향 프로그래밍 (Object Oriented Programming)
    - 객체 지향 언어이며, 모든 것이 객체로 구현

<br/>

## 객체와 변수

<br/>

- ### **`객체 (Object)`**
  - 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것
  
<br/>

- ### **`변수`**
  - 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조
  - 동일 이름에 다른 객체를 언제든 할당 가능
  - ```
    x와 y의 값을 바꾸는 방법
    1. z = x
       x = y
       y = z
    
    2. x, y = 1, 2
      (파이썬은 이 코드가 가능함)
    ```

<br/>

- ### **`식별자 (identifiers)`**
  - 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름
  - 규칙
    - 영문 알파벳, _ , 숫자로 구성
    - 첫 글자에 숫자 x
    - 길이제한 x, 대소문자를 구별
    - 예약어 사용 불가 (ex/ False, break, for 등등)

<br/>

- ### **`자료형 (Data Type)`**
  - 숫자
    - 수치형 (int, float, complex)
    - 불린형
  - 시퀀스 (Sequence)
    - 문자열(String)
    - 튜플(Tuple)
    - 리스트(List)
    - 레인지(Range)
  - 컬렉션 (Collection)
    - 집합(Set)
    - 딕셔너리(Dictionary)
  - None

<br/>

- ### **`수치형 (Numeric Type)`**
  - 정수(Int)
    - 모든 정수의 타입은 int
    - 오버플로우 발생 x
  - 실수(Float)
    - 정수가 아닌 모든 실수는 float
    - 부동소수점
      - 실수 연산 과정에서 에러 발생 가능성 있음
    - 복소수(Complex)
      - 허수는 j로 표현

<br/>

- ### **`불린형 (Boolean Type)`**
  - True / False 값을 가진 타입은 bool
  - 비교 / 논리 연산을 수행할 때 활용
  - 0, 0.0, (), {}, [] == None

<br/>

- ### **`연산자 (Operator)`**
  - 산술 연산자(Arithmetic Operator)
    ```
    +   덧셈
    -   뺄셈
    *   곱셈
    %   나머지
    /   나눗셈
    //  몫
    **  거듭제곱
    ```
  - 복합 연산자(In-place Operator)
    ```
    a += b    a = a + b
    a -= b    a = a - b
    a *= b    a = a * b
    a %= b    a = a % b
    a /= b    a = a / b
    a //= b   a = a // b
    a **= b   a = a ** b
    ```
  - 비교 연산자(Comparison Operator)
    ```
    <   미만
    <=  이하
    >   초과
    >=  이상
    ==  같음
    !=  같지않음
    ```

  - 논리 연산자 (Logical Operator)
    ```
    A and B   A와 B 모두 True시, True
    A or B    A와 B 모두 False시, False
    Not       True를 False로, False를 True로

    True and True     True
    True and False    False
    False and True    False
    False and False   False

    True or True      True
    True or False     True
    False or True     True
    False or False    False

    not True          False
    not False         True
    ```

<br/>

- ### **`컨테이너`**
  - 여러 개의 값을 담을 수 있는 것
  - 순서가 있음
  - 시퀀스
    - 문자열(immutable) : 문자들의 나열
    - 리스트(mutable) : 변경 가능한 값들의 나열
    - 튜플(immutable) : 변경 불가능한 값들의 나열
    - 레인지(immutable) : 숫자의 나열
  - 컬렉션 / 비시퀀스
    - 세트(mutable) : 유일한 값들의 모음
    - 딕셔너리(mutable) : 키-값들의 모음

<br/>

- ### **`시퀀스형 컨테이너 (Sequence Container)`**
  - 주요 공통 연산자
    ```
    s[i]          s의 i번째 항목, 0에서 시작
    s[i:j]        s의 i에서 j까지의 슬라이스
    s[i:j:k]      s의 i에서 j까지 스텝 k의 슬라이스
    s+t           s와 t의 이어 붙이기
    s*n 또는 n*s  s를 그 자신에 n번 더하는 것
    x in s        s의 항목 중 하나가 x와 같으면 True (or False)
    x not in s    s의 항목 중 하나가 x와 같으면 False (or True)
    len(s)        s의 길이
    min(s)        s의 가장 작은 항목
    max(s)        s의 가장 큰 항목
    ```

<br/>

- ### **`문자열 (String Type)`**
  - 모든 문자는 str 타입
  - 문자열은 " or ' 활용
  - 변경 불가능(immutable)
  - 반복 가능(iterable)

<br/>

- ### **`중첩따옴표 (Nested Quotes)`**
  - 큰 따옴표 안에선 작은 따옴표로 문자열 생성
  - 작은 따옴표 안에선 큰 따옴표로 문자열 생성

<br/>

- ### **`삼중따옴표 (Triple Quotes)`**
  - 따옴표 3개 사이에 작은 따옴표나 큰 따옴표를 입력해 문자열 생성

<br/>

- ### **`인덱싱`**
  - str = [abcdefg] / str[0] = 'a' / str[1] = 'b'

<br/>

- ### **`슬라이싱`**
  - str = [abcdefg] / str[2:5] = 'cde' / str[2:5:2] = 'ce'

<br/>

- ### **`결합 (concatenation)`**
  - 'hello' + 'world!' = 'hello world!'

<br/>

- ### **`반복 (Repetition)`**
  - 'hi!' * 3 = 'hi!hi!hi!'

<br/>

- ### **`포함 (Membership)`**
  - 'a' in 'apple' = True / 'b' in 'apple' = False

<br/>

- ### **`Escape sequence`**
  - 역슬래시를 활용
    ```
    \n    줄 바꿈
    \t    탭
    \r    캐리지리턴
    \O    널(Null)
    \\    \
    \'    단일인용부호 '
    \"    이중인용부호 "
    ```

<br/>

- ### **`리스트 (List)`**
  - 변경 가능한 값들의 나열된 자료형
  - 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
  - 변경 가능(mutable), 반복 가능(iterable)
  - 항상 대괄호[] 형태로 정의, 요소는 ,로 구분
  - 예시
    ```
    생성
    my_list = []
    another_list = list()

    접근
    a = [1, 2, 3]
    print(a[0]) # 1

    변경
    a[0] = '1'
    print(a) # ['1', 2, 3]

    추가
    a.append(4) # ['1', 2, 3, 4]

    삭제
    a.append(0) # [2, 3, 4]

    활용 예제
    boxes = ['apple', 'banana']
    len(boxes) # 2
    boxes[1] # 'banana'
    boxes[1][0] # 'b'
    ```

<br/>

- ### **`None`**
  - 파이썬 자료형 중 하나
  - 값이 없음을 표현
  - 반환 값이 없는 함수에서 사용되기도 함

<br/>

## 파이썬 사용 관련 안내

<br/>

- 대소문자 구분
- 띄어쓰기, 문장부호 주의
- 문장 구분 시, 들여쓰기 사용
- 주석 처리 # (Ctrl + /)
- input('이름을 입력해주세요 : ')
- int(input('숫자를 입력해주세요 : ')) / str형이나 int형 주의