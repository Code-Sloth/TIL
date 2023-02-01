# 8강

<br/>

## DFS(Depth-First Search)
- 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 자료구조(혹은 재귀함수)를 이용
  - 탐색 시작 노드를 스택에 삽입하고 방문 처리
  - 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
  - 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
- 번호가 낮은 인접 노드부터

```python
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
visited = [False] * 9
dfs(graph, 1, visited)
# 1 2 7 6 8 3 4 5 
```
```python
def dfs(v):
  vi[v] = 1
  print(v)
  for i in g[v]:
    if not vi[i]:
      dfs(i)
```


<br/>

## BFS(Breadth-First Search)
- 너비 우선 탐색, 가까운 노드부터 우선적으로 탐색하는 알고리즘
- 큐 자료구조를 이용
  - 탐색 시작 노드를 큐에 삽입하고 방문 처리
  - 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
  - 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
- 번호가 낮은 인접 노드부터

```python
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
visited = [False] * 9
bfs(graph, 1, visited)
# 1 2 3 8 7 4 5 6
```
```python
def bfs(v):
  q = deque([v])
  vi[v] = 1
  while q:
    v = q.popleft()
    print(v)
    for i in g[v]:
      if not vi[i]:
        q.append(i)
        visited[i] = 1
```

<br/>

# 9강

<br/>

## 기초 문제 풀이

<br/>

### 문제 1 (음료수 얼려 먹기)
N * M 크기의 얼음틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 다음의 4 X 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

입력 :
4 5
00110
00011
11111
00000

출력 :
3

```python
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().strip())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
```

<br/>

### 문제 2 (미로 탈출)

N x M 크기의 직사각형 형태의 미로에 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 현재 위치는 (1, 1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

입력 :
5 6
101010
111111
000001
111111
111111

출력 :
10

```python
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().strip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))
```
