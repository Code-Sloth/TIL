# 시간 복잡도(Time Complexity)

<br/>

- 계산 복잡도 이론에서 시간 복잡도는 문제를 해결하는데 걸리는 시간과 입력의 함수 관계를 가리킨다

<br/>

## 알고리즘의 시간 복잡도

<br/>

- 개개인마다 같은 알고리즘이라도 측정 시간이 달라 객관적인 기준이 필요
- 객관적인 측정을 위해 알고리즘 내부에서 기본연산 횟수 파악

<br/>

### **`시간 복잡도 계산`**

<br/>

```python
# 총 시간 : k
statement 1
statement 1
statement 1
  ...
statement k

# 총 시간 : max(1,2)
if ~~:
  code 1
else:
  code 2

# 총 시간 : N
for i in range(N):
  code

# 총 시간 : N * M
for i in range(N):
  for j in range(M):
    code

# 총 시간 : N + M
for i in range(N):
  code 1
for j in range(M):
  code 2

# 총 시간 : N * N + N
for i in range(N):
  for j in range(N):
    code 1
for k in range(N):
  code 2

# 총 시간 : N + N+1 + ... 1 # (N+1)N/2
for i in range(N):
  for j in range(i, N):
    code
```

<br/>

## 빅오(Big-O) 표기법

<br/>

- 입력 n이 무한대로 커진다고 가정하고 시간 복잡도를 간단히 표시하는 것
- 최고차항만 남기고 계수와 상수 제거 (3n == 6n)
- 일반적인 상황에서 1초가 걸리는 입력의 크기
  - O(1) : // 단순 산술 계산
  - O(N) : 1억(기준) // 크기 N인 리스트 순회
  - O(logN) : // 크기 N인 리스트를 반절씩 순회/탐색
  - O(N*logN) : 500만 // 크기 N인 리스트를 반절씩 탐색/순회
  - O(N^2) : 1만 // 크기 N,N인 이중 리스트를 순회
  - O(N^3) : 500 // 3중 리스트 순회
  - O(2^N) : 20 // 크기 N집합의 부분 집합
  - O(N!) : 10 // 크기 N리스트의 순열
- 내장함수의 중첩 for문 생각

<br/>

![big o 1](https://raw.githubusercontent.com/Code-Sloth/TIL/master/kdt_week4/image/bigo1.png)

<br/>

![big o 2](https://raw.githubusercontent.com/Code-Sloth/TIL/master/kdt_week4/image/bigo2.png)