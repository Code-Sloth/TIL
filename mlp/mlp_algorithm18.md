# 표준 라이브러리

<br/>

## 실전에서 유용한 표준 라이브러리
- 내장 함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공
  - 파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능 포함
- itertools : 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들 제공
  - 특히 순열, 조합 라이브러리는 코테에서 자주 사용
- heapq : 힙 자료구조를 제공
  - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
- bisect : 이진 탐색 기능을 제공
- collections : 덱, 카운터 등의 유용한 자료구조 포함
- math : 필수적인 수학적 기능을 제공
  - 팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이와 같은 상수를 포함

<br/>

### 자주 사용되는 내장 함수
- sum : 합
- min, max : 최소, 최대
- eval : 문자열 식을 계산
- sorted : 정렬
- sorted with key : key 속성으로 정렬

<br/>

### 순열과 조합
- 모든 경우의 수를 고려해야 할 때 효과적으로 사용
- 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열
  - A,B,C ==> ABC ACB BAC BCA CAB CBA
  - nPr = n*(n-1)*(n-2)*...*(n-r+1)
```python
# 순열
from itertools import permutations
a = ['A','B','C']
print(list(permutations(a,3)))

# 중복 순열
from itertools import product
a = ['A','B','C']
print(list(product(a,3)))
```
- 조합 : 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택
  - A,B,C ==> AB, AC, BC
  - nCr = (n*(n-1)*(n-2)*...*(n-r+1))/r!
```python
# 조합
from itertools import combinations
a = ['A','B','C']
print(list(combinations(a,2)))

# 중복 조합
from itertools import combinations_with_replacement
a = ['A','B','C']
print(list(combinations_with_replacement(a,2)))
```

<br/>

### Counter
- collecitons 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공
- 리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇번씩 등장했는지
```python
from collections import Counter
a = Counter([1,2,3,4,1,2])
print(a[1])
print(a[2])
print(dict(a))
# 2
# 2
# {1: 2, 2: 2, 3: 1, 4: 1}
```

<br/>

# 최대 공약수와 최대 공배수
- math 라이브러리의 gcd() 함수 이용
```python
import math
def lcm(a,b):
  return a*b // math.gcd(a,b)
a = 21
b = 14
print(math.gcd(21,14))
print(lcm(21,14))
# 7
# 42
```