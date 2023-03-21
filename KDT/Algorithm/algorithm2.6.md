# 깊이 우선 탐색(DFS)

<br/>

## 그래프 탐색 알고리즘
- 시작 정점에서 간선을 타고 이동할 수 있는 모든 정점을 찾는 알고리즘
- DFS(스택), BFS(큐)

<br/>

## DFS
- 시작 정점으로부터 갈 수 있는 하위 정점까지 가장 깊게 탐색하고 더 이상 갈 곳이 없다면 마지막 갈림길로 돌아와서 다른 정점을 탐색하여 결국 모든 정점을 방문하는 순회 방법
- 모든 정점을 방문할 때 유리, 경우의 수, 순열과 조합 문제에서 많이 사용
- BFS에 비해 코드 구현이 간단

<br/>

### DFS 동작 과정
- 각 정점을 방문했는지 여부를 판별할 방문 체크 리스트가 필요
- 사이클
  - 현재 정점 방문처리
  - 인접한 모든 정점 확인
  - 방문하지 않은 인접 정점 이동

<br/>

### 코드 구현
```python
def dfs(v):
  vi[v] = 1
  print(v)
  for i in g[v]:
    if not vi[i]:
      dfs(i)
```

<br/>

### 추천 문제
- [BOJ 2606 바이러스](https://www.acmicpc.net/problem/2606)

<br/>

### 이차원 격자에서의 DFS
```python
def dfs(i,j):
    global t
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if g[i][j]:
        g[i][j] = 0
        for dx, dy in d:
            nx, ny = i + dx, j + dy
            dfs(nx,ny)
        return True
    return False
```