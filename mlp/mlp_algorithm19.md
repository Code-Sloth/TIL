# 소수 (Prime Number)

<br/>

### 기본적인 알고리즘
```python
def is_prime(x):
  for i in range(2,x):
    if x % i == 0:
      return False
  return True
```

<br/>

### 소수의 판별 알고리즘 성능 분석
- 2부터 x-1까지의 모든 자연수에 대해서 연산을 수행
  - 시간 복잡도 O(X)

<br/>

### 약수의 성질
- 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭
- 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 됨
```python
import math
def is_prime(x):
  for i in range(2, int(math.sqrt(x))+1): # int(x**0.5)+1
    if x % i == 0:
      return False
  return True
```
- 시간 복잡도 O(N^1/2)

<br/>

### 다수의 소수 판별
- 특정한 수의 범위 안에 존재하는 모든 소수를 찾아야 하는 방법
  - 에라토스테네스의 체 알고리즘 사용

<br/>

### 에라토스테네스의 체
- 다수의 자연수에 대하여 소수 여부를 판별할 때 사용
- N보다 작거나 같은 모든 소수를 찾을 때 사용
- 구체적인 동작 과정
  - 2부터 N까지의 모든 자연수를 나열
  - 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾음
  - 남은 수 중에서 i의 배수를 모두 제거(i 제외)
  - 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복
```python
import math

n = 1000
arr = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
  if arr[i] == True:
    j = 2
    while i * j <= n:
      arr[i*j] = False
      j += 1

for i in range(2, n+1):
  if arr[i]:
    print(i, end = ' ')
```

<br/>

### 에라토스테네스의 체 알고리즘 성능 분석
- 사실상 선형 시간에 가까울 정도로 매우 빠름
  - 시간 복잡도 O(NloglogN)
- 다수의 소수를 찾아야 하는 문제에서 효과적으로 사용
  - 하지만 각 자연수에 대한 소수 여부를 저장해야 하므로 메모리가 많이 필요
