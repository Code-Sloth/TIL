# 재귀 함수(Recursive Function)

<br/>

## 재귀 함수
- 자기 자신을 다시 호출하는 함수
- 최대 재귀 깊이 늘리기
```python
import sys
sys.setrecursionlimit(10*9)
```
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야함
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음
  - 종료 조건을 포함한 재귀 함수 예제
  ```python
  def rfunc(i):
    if i = 100: return
    print(i,i+1)
    rfunc(i+1)
    print(i)
  rfunc(1)
  ```

<br/>

### 팩토리얼 구현 예제
- n!
- 수학적으로 0!, 1!의 값은 1
```python
# 반복 구현
def fac(n):
  t = 1
  for i in range(1, n+1):
    t *= i
  return t

# 재귀 구현
def fac(n):
  if n <= 1: return 1
  return n * fac(n-1)
```

### 최대공약수 계산(유클리드 호제법) 예제
- 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘
- 두 자연수 A,B (A>B) A를 B로 나눈 나머지를 R
- 이 때 A와 B의 최대 공약수는 B와 R의 최대공약수와 동일
```python
# 반복 구현
def gcd(a,b):
  while b > 1:
      a, b = b, a%b
  return a
print(gcd(a,b))

# 재귀 구현
def gcd(a,b):
  if a%b == 0: return b
  else: return gcd(b, a&b)
print(gce(n,m))
```

<br/>

### 재귀 함수 사용 유의 사항
- 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성 가능
  - 단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있음
- 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현 가능
- 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 존재
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
  - 그래서 스택을 사용해야 할 때 구현 상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많음
