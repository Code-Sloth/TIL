# 함수


<br/>

- 함수를 사용하는 이유는 복잡한 내용을 숨기고 재사용성, 가독성, 생산성때문이다.

<br/>

## 함수 기초

<br/>

### **`함수의 정의`**

<br/>

- 특정한 기능을 하는 코드의 묶음
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에 호출
- 사용자 함수(Custom Function)
  - 구현되어 있는 함수가 없는 경우, 사용자가 직접 작성
- 내장 함수(Built-in Function)

<br/>

### **`함수의 기본 구조`**

- ```
  def pstdev(data, mu=None):
  
  def = keyword
  pstdev = name
  data, mu=None = parameters
  ```
- 선언과 호출 / 입력 / 범위 / 결과값

<br/>

### **`내장 함수`**

<br/>

- print, len, sum, max, pow, all 등등 많이 존재
- [파이썬 내장함수](https://docs.python.org/ko/3/library/functions.html)

<br/>

### **`함수 응용`**

- map(function, iterable)
  - 순회 가능한 데이터구조의 모든 요소에 함수적용하고, 그 결과를 map object로 반환

<br/>

## 수업 추가 설명

<br/>

- ### **`print(*objects)`**
  - *objects : *은 여러 값을 무한하게 받을 수 있다.

```
print('hi')
print('hi', 'hello')
print('hi', 'hello', 'guten tag')

# print(sep=' ', end='\n')
# sep=' ' : sep라는 키워드는 기본 값이 space 
# end='\n' : end라는 키워드는 기본 값이 개행
print('hi', 'hello', sep='!')
print('hi', end='')
print('hello')

# print 함수는 반환 값이 없다
print(print('hi')) # None
```

<br/>

- ### **`sum`**
  - sum 함수는 합을 반환

```
print(sum([1,2,3])) # 6

# 1부터 입력받은 숫자까지의 합
print(sum(range(1, int(input())+1)))
```

<br/>

- ### **`len`**
  - 길이를 알 수 있는 함수

```
numbers = [10, 20, 5]

# 길이?
cnt = 0 
for number in numbers:
    cnt += 1 
print(cnt)

# 함수!
print(len(numbers))
```

<br/>

- ### **`ord / chr`**
  - 유니코드로 전환 / 문자열로 전환
  
```
print(ord('a'))
print(chr(97))
```

<br/>

- ### **`sort`**
  - sort = list를 정렬
  - sorted = 모든 반복 가능한 작업에 적용 가능

```
a = [10, 20, 5]
print(sorted(a))
```

<br/>

- ### **`함수 객체`**
  - 함수는 그 자체로 객체이다.

```
print(len)
print(type(len))
```

<br/>

- ### **`map`**
  - 첫번째 인자(Input)으로 함수를 받아서 두번째 인자(Input)인 반복 가능한 객체의 모든 요소에 적용!

```
numbers = ['1', '2', '3']
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

numbers = ['1', '2', '3']
new_new_numbers = map(int, numbers)
print(new_new_numbers)
print(list(new_new_numbers))

a = input()
print(a) # '2 5'
# 원하는 것은 숫자 2와 숫자 5

# 1. 문자열을 각각 쪼갠 요소를 가진 리스트로 변환 -> .split()
b = a.split()
print(b) # ['2', '5']

# 2. 각 요소를 숫자로 변환 -> map()
c = map(int, b)
print(c) # map 

# 3. 각각 변수에 저장
d, e = list(c) # list(c)가 [2, 5]
print(d, e) # 각각 2, 5

# 결론 -  다 합치면
numbers = list(map(int, input().split()))
```