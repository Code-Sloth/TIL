# 문제 접근 알고리즘

<br/>

## 유클리드 호제법 (최대 공약수)

<br/>

- 2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘
- 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻음
- 78696과 19332의 최대 공약수
  - 78696 = 19332x4 + 1368
  - 19332 = 1368x14 + 180
  - 1368 = 180x7 + 108
  - 180 = 108x1 + 72
  - 108 = 72x1 + 36
  - 72 = 36x2
  - 따라서 최대 공약수는 36
- 함수 코드

```python
def func(a,b):
  while b > 0:
    a, b = b, a % b
  return a
```

<br/>

## 에라토스테네스의 체 (소수)

<br/>

- 소수의 여부를 확인 할 때, 제곱근까지만 검증 / 시간 복잡도 : O(N^1/2)
- 대량의 소수를 한꺼번에 판별할 때 에라토스테네스의 체 이용
- 배열 할당 후 해당 값 넣고 하나씩 지워가는 방법
- 함수 코드 (1부터 100까지 소수 구하는 코드)

```python
# 일반적인 소수 구하는 코드
n = 100

def is_prime(a):
    if a < 2:
        return False
    for i in range(2,a):
        if a % i == 0:
            return False
    return True

for i in range(n+1):
    if is_prime(i):
        print(i,end = ' ')
# 2 3 5 7 11 13 17 19 23 29 31 37 41 
# 43 47 53 59 61 67 71 73 79 83 89 97

# 에라토스테네스의 체 이용 ()
n = 100

def is_prime(n):
    li = [True] * n
    
    for i in range(2,int(n**0.5)+1):
        if li[i] == True:
            for j in range(2*i, n, i):
                li[j] = False
    return [num for num in range(2,n) if li[num] == True]
sol = is_prime(n)
print(sol,end = ' ')
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 

# m에서 n까지 개수 파악
import bisect
print(bisect.bisect(sol,n) - bisect.bisect(sol,m))
# 21
```