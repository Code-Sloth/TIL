# 파이썬 속도 개선 방법

<br/>

## 적절한 자료구조의 사용
- in 연산을 사용할 때 가장 적합한 자료구조 : set / 시간 복잡도 - O(1)
- 딕셔너리를 사용할 때는 데이터 초기화 작업이 dict보다 빠른 defaultdict를 사용
```python
from collections import defaultdict

s = 'apple'
int_dict = defaultdict(int)

for st in s:
    int_dict[st] += 1
print(int_dict)
# defaultdict(<class 'int'>, {'a': 1, 'p': 2, 'l': 1, 'e': 1})

li = [('a',1),('b',2),('c',3),('a',4),('b',5),('a',1)]
list_dict = defaultdict(list)

for k,v in li:
    list_dict[k].append(v)
print(list_dict)
# defaultdict(<class 'list'>, {'a': [1, 4, 1], 'b': [2, 5], 'c': [3]})

li = [('a',1),('b',2),('c',3),('a',4),('b',5),('a',1)]
set_dict = defaultdict(set)

for k,v in li:
    set_dict[k].add(v)
print(set_dict)
# defaultdict(<class 'set'>, {'a': {1, 4}, 'b': {2, 5}, 'c': {3}})
```

<br/>

## 리스트 컴프리헨션을 제너레이터 표현으로 대체
- 제너레이터 표현식은 이터레이터를 메로리제 저장하지 않고 결과를 얻어 공간 복잡도를 줄이는 효과
```python
import sys

# 리스트 컴프리핸션 (bad)
nums_sum_list_comprehension = sum([num ** 2 for num in range(1000000)])

# 제네레이터 표현식 (good)
nums_sum_generator_expression = sum((num ** 2 for num in range(10000000)))

# Bad
nums_squared_list = [num ** 2 for num in range(1000000)]
print(sys.getsizeof(nums_squared_list))  # 87632

# Good
nums_squared_generator = (num ** 2 for num in range(1000000))
print(sys.getsizeof(nums_squared_generator))  # 128
```

<br/>

## 글로벌 변수는 로컬 변수로 대체
- 글로벌 변수의 사용은 시스템의 심각한 오류를 야기
- 실행 속도 또한 로컬 변수에 비해 느림


<br/>

## 데이터 중복 피하기
- 의미 없는 데이터 복사는 피하는게 좋음
```python
# bad
a, b = 10, 15
temp = a
a = b
b = temp
print(a,b)

# good
a, b = 10,15
a, b = b, a
print(a,b)
```
- 문자열을 붙일 때는 +연산 대신 join() 사용
  - str 은 변경할 수 없는 객체이기 때문에 + 연산을 하는 경우 각각의 문자열을 새로운 메모리 공간에 복사하여 작업을 수행
  - join() 함수를 사용할 경우 문자열 병합에 필요한 총 메모리 공간을 미리 계산한 뒤 필요한 메모리를 확보 후 해당 공간에 각각의 문자열을 복사

<br/>

## if문의 조건 순서 변경
- and 일 경우 False값을 많이 가진 조건을 앞으로 배치하면 뒤의 조건문에 대한 확인 작업을 피할 수 있음
- or 일 경우 True값을 많이 가진 조건을 앞으로 배치하면 뒤의 조건문에 대한 확인 작업을 피할 수 있음
