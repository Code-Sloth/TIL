# Python 제어문 (조건문 및 반복문)

<br/>

## String Formatting

- 문자열을 변수를 활용하여 만드는 법
- ```
  ex) 
  name = 'kim'
  age = 28
  print(f'이름 : {name}이고 나이 : {age}살이다.')
  ```

<br/>
<br/>

## 형 변환 (Typecasting)

<br/>
<br/>

### **`자료형 변환(Typecasting)`**

- 파이썬에서는 데이터 형태는 서로 변환 가능
- 암시적 형 변환(Implicit Typecasting)
  - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환
  - bool / Numeric type(int, float, complex)
  - ```
    True + 3
    # 4
    3 + 5.0
    # 8.0
    3 + 4j + 5
    # (8+4j)
    ```

    <br/>

- 명시적 형 변환(Explicit Typecasting)
  - 사용자가 특정 함수를 활용해 의도적으로 자료형을 변환
  - ```
    문자열은 암시적 타입 변화 x
    '3' + 4
    명시적 타입 변환이 필요함
    int('3') + 4
    정수 형식이 아닌 경우 타입 변화 불가능
    int('3.5') + 5
    가능
    float('3.5') + 5
    ```

<br/>

## 제어문 (Control Statement)

<br/>

- 파이썬은 기본적으로 위에서부터 아래로 순차적 명령 수행
- 특정 상황에 따라 코드를 선택적으로 실행하거나 반복하는 제어가 필요
- 제어문은 순서도(flow chart)로 표현 가능

<br/>
<br/>

### **`조건문 (Conditional Statement)`**

<br/>

- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용
  - ```
    if < expression >:
      # Run this Code block
    elif < expression >:  # (복수 조건문)
      # Run this Code block
    else:
      # Run this Code block
    ```

<br/>

### **`중첩 조건문`**

- 조건문은 다른 조건문에 중첩되어 사용될 수 있음 (들여쓰기 유의)
  - ```
    if < expression >:
      # Code block
        if < expression >:
          # Code block
    else:
      # Code block
    ```

<br/>

### **`레인지(Range)`**

- 숫자의 시퀀스를 나타내기 위해 사용
  - range(n,m,s) / n부터 m-1까지 증가시키며 숫자의 시퀀스
- 변경 불가능(immutable) / 반복 가능(iterable)
- ```
  list(range(3))
  # [0, 1, 2]
  list(range(1, 5))
  # [1, 2, 3, 4]
  list(range(1, 5, 2))
  # [1, 3]
  ```

<br/>

### **`반복문`**

- 특정 조건을 도달할 때까지 계속 반복되는 일련의 문장

<br/>

### **`While문`**

- 조건식이 참인 경우 반복적으로 코드 실행
- 무한 루프를 하지 않도록 종료조건이 반드시 필요
- ```
  a = 0
  while a < 5:
    print(a)
    a += 1
  print('끝')

  1부터 사용자가 입력한 양의 정수까지의 총합
  n = 0
  total = 0
  user_input = int(input())
  while n <= user_input:
    total += n
    n += 1
  print(total)
  ```

<br/>

### **`for문`**

- 시퀀스(string,tuple,list,range)를 포함한 순회가능한 객체요소를 모두 순회
- 처음부터 끝까지 모두 순회하므로 종료조건 필요 x
- 순회 가능 객체 : 컨테이너형(string,list,tuple,range,set,dictionary)
- ```
  for fruit in ['apple', 'mango', 'banana']
    print(fruit)
  print('끝')

  문자열 순회
  chars = input()
  for i in range(len(chars)):
    print(chars[i])
  ```

<br/>

### **`반복문 제어`**

- break
  - 반복문을 종료
- continue
  - continue 이후의 코드 블록은 수행x, 다음 반복을 수행
- for-else
  - 끝까지 실행한 이후에 else문 실행
  - break로 중간에 종료되는 경우 else문 실행 x
- ```
  # break
  n = 0
  while True:
    if n == 3:
      break
    print(n)
    n += 1

  for i in range(10):
    if i > 1:
      print('0과 1만 필요')
      break
    print(i)

  # continue
  for i in range(6):
    if i % 2 == 0:
      continue
    print(i)

  # for-else
  for char in 'banana'
    if char == 'b':
      print('b!')
      break
  else:
    print('b가 없습니다.')
  ```