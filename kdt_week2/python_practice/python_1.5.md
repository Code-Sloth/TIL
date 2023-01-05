# 컬렉션

<br/>

## 딕셔너리(Dictionary)

<br/>

- 키-값(key-value) 쌍으로 이뤄진 모음(collection)
  - 키(key)
    - 불변 자료형만 가능 (list,dict등은 불가능)
  - 값(values)
    - 어떠한 형태든 관계없음
- 키와 값은 : 로 구분 / 개별 요소는 , 로 구분
- 변경 가능(mutable), 반복 가능(iterable)

<br/>

### **`딕셔너리 생성`**

- key와 value가 쌍으로 이뤄진 자료구조
  - key는 변경 불가능한 데이터만 활용 가능
    - string, integer, float, boolean, tuple, range
  - value는 모든 값 가능

<br/>


### **`딕셔너리 키-값 추가 및 변경`**

- 딕셔너리에 키와 값의 쌍을 추가할 수 있다
- 이미 해당하는 키가 있다면 기존 값이 변경

<br/>

### **`딕셔너리 키-값 삭제`**

- 키를 삭제하고자 하면 .pop()을 활용하여 삭제 (d.pop(key))

<br/>

### **`딕셔너리 순회`**

- 반복문에서 딕셔너리는 기본적으로 key를 순회
- items() : (key, value) 의 튜플
  ```
  d = {'a' : 1, 'b' : 2}

  print(d.keys())
  print(d.values())
  print(d.items())

  for key,value in d.items():
    print(key, value)
  ```

<br/>

## 모듈

- 특정 기능을 하는 코드를 파이썬 파일(.py)단위로 작성한 것

<br/>

## 패키지

- 특정 기능과 관련된 여러 모듈의 집합
- 패키지 안에는 또 다른 서브 패키지를 포함

<br/>

## 파이썬 표준 라이브러리

<br/>

### **`Random(import random)`**

<br/>

- 숫자/수학 모듈 중 의사 난수 생성
- random.randint(a,b)
  - a 이상 b이하의 임의의 정수 N을 반환
- random.chice(seq)
  - 비지 않은 시퀀스에서 임의의 요소를 반환
- random.shuffle(seq)
  - 시퀀스를 제자리에서 섞는다
- random.sample(population, k)
  - 무작위 비복원 추출한 결과인 k 길이의 리스트를 반환

<br/>

### **`Datetime(import datetime)`**

<br/>

- 날짜와 시간을 조작하는 객체를 제공
- datetime.date(y,m,d)
  - 모든 인자가 필수, 인자는 특정 범위에 있는 정수
- datetime.date.today()
  - 현재 지역 날짜를 반환
- datetime.datetime.today()
  - 현재 지역 datetime을 반환 / now는 현재 타임존

<br/>

### **`OS`**

<br/>

- OS(운영체제)를 조작하기 위한 인터페이스 제공
- os.listdir(path='.')
  - path에 의해 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트반환
  - 리스트는 임의의 순서로 나열, 특수 항목 포함x
- os.mkdir(path)
  - path라는 디렉토리 생성
- os.chdir(path)
  - path를 변경

<br/>

## 에러/예외 처리

<br/>

### **`문법 에러`**

<br/>

### **`예외`**

- 실행 도중 예상치 못한 상황이 오면 프로그램 실행을 멈춤
- 실행 중에 감지되는 에러들 = 예외(exception)

<br/>

### **`예외 발생`**

- raise / assert