# 이차원 리스트

- 리스트를 원소로 가지는 리스트
- 행렬을 나타낼 수 있음
- n x m 행렬
```python
li = [[0] * m for i in range(n)]
```

<br/>

## 순회
- 전체 순회
```python
for i in range(n):
  for j in range(m):
    print(li[i][j])
```
- Pythonic한 방법으로 이차원 리스트의 총합 구하기
```python
total = sum(map(sum,li))
```
- Pythonic한 방법으로 이차원 리스트의 최대값, 최소값 구하기
```python
max_li = max(map(max,li))
min_li = min(map(min,li))
```

<br/>

## 전치
- 전치란 행과 열을 서로 맞바꾸는 것을 의미
```python
li2 = [[0] * n for i in range(m)]
for i in range(n):
  for j in range(m):
    li2[i][j] = li[j][i]
```

<br/>

## 회전
- 왼쪽으로 90도 회전
```python
li2 = [[0] * n for i in range(n)]
for i in range(n):
  for j in range(n):
    li2[i][j] = li[j][n-j-1]
```
- 오른쪽으로 90도 회전
```python
li2 = [[0] * n for i in range(n)]
for i in range(n):
  for j in range(n):
    li2[i][j] = li[n-j-1][i]
```

