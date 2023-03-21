# 완전 탐색(Exhaustive Search)

<br/>

## Brute-force
- 모든 경우의 수를 탐색하여 문제를 해결하는 방식

<br/>

### 추천 문제
- [2798 블랙잭](https://www.acmicpc.net/problem/2798)

<br/>

## 델타 탐색(Delta Search)
- 이차원 리스트의 완전 탐색에서 많이 등장하는 유형
- 모든 원소를 순회하며 각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동
```python
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# [(-1,0), (1,0), (0,-1), (0,1)]로 써서 해도 됨
# 대각선까지 델타값
# dx = [-1,1,0,0,-1,1,-1,1]
# dy = [0,0,-1,1,-1,-1,1,1]

for x in range(n):
  for y in range(m):
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        x = nx
        y = ny
```
