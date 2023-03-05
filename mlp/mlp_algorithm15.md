# 최소 공통 조상 : 트리에서의 최소 공통 조상을 찾는 알고리즘

<br/>

## 최소 공통 조상 (Lowest Common Ancestor) : 기초 문제
- BOJ 'LCA' 문제
- N(2 ≤ N ≤ 50,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다. 두 노드의 쌍 M(1 ≤ M ≤ 10,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

<br/>

### 기본적인 최소 공통 조상(LCA) 알고리즘
1. 모든 노드에 대한 깊이를 계산
2. 최소 공통 조상을 찾을 두 노드를 확인
  1. 먼저 두 노드의 깊이가 동일하도록 거슬러 올라감
  2. 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라감
3. 모든 LCA(a,b) 연산에 대하여 2번의 과정을 반복

<br/>

### 기본적인 최소 공통 조상 알고리즘 연산 과정
- DFS를 이용해 모든 노드에 대하여 깊이를 계산
- LCA
  - 먼저 두 노드의 깊이를 맞춤
  - 이후에 거슬러 올라감
```python
import sys
sys.setrecursionlimit(10*6)
n = int(input())

parent = [0] * (n+1) # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
g = [[] for _ in range(n+1)] # 그래프 정보

for _ in range(n-1):
  a,b = map(int,input().split())
  g[a].append(b)
  g[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, d):
  c[x] = True
  d[x] = d
  for y in g[x]:
    if c[y]:
      continue
    parent[y] = x
    dfs(y, d+1)

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a,b):
  while d[a] != d[b]:
    if d[a] > d[b]:
      a = parent[a]
    else:
      b = parent[b]
  
  while a != b:
    a = parent[a]
    b = parent[b]
  return a

dfs(1,0)

m = int(input())
for i in range(m):
  a, b = map(int,input().split())
  print(lac(a,b))
```

<br/>

### 시간 복잡도 분석
- 매 쿼리마다 부모 방향으로 거슬러 올라가기 위해 최악의 경우 O(N)
  - 따라서 모든 쿼리를 처리할 때의 시간 복잡도 O(NM)

<br/>

## 최소 공통 조상 심화 문제
- BOJ 'LCA 2'문제
- N(2 ≤ N ≤ 100,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다. 두 노드의 쌍 M(1 ≤ M ≤ 100,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.
- 각 노드가 거슬러 올라가는 속도를 빠르게 만드는 방법
  - 만약 총 15칸 거슬러 올라가야 한다면
    - 8칸 > 4칸 > 2칸 > 1칸
- 2의 제곱 형태로 거슬러 올라가도록 하면 O(logN)의 시간복잡도를 보장
- 메모리를 좀 더 사용하여 각 노드에 대하여 2^i번째 부모에 대한 정보를 기록

<br/>

### 개선된 최소 공통 조상 알고리즘
- 메모리는 더 크지만 시간을 줄임
- 모든 노드에 대하여 깊이와 2^i번째 부모에 대한 정보를 계산
- 두 노드의 깊이를 맞춤
- 이후에 거슬러 올라감

<br/>

### 시간 복잡도 분석
- 다이나믹 프로그래밍을 이용해 시간 복잡도를 개선
  - 세그먼트 트리를 이용하는 방법도 존재
- 매 쿼리마다 부모를 거슬러 올라가기 위해 O(logN)의 복잡도가 필요
  - 따라서 모든 쿼리를 처리할 때의 시간 복잡도는 O(MlogN)
```python
import sys
imput = sys.stdin.readline
sys.setrecursionlimit(10*6)
log = 21 # 2^20

n = int(input())
parent = [[0] * log for _ in range(n+1)] # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
g = [[] for _ in range(n+1)] # 그래프 정보

for _ in range(n-1):
  a,b = map(int,input().split())
  g[a].append(b)
  g[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x,d):
  c[x] = True
  d[x] = d
  for y in g[x]:
    if c[y]:
      continue
    parent[y][0] = x
    dfs(y,d+1)

# 전체 부모 관게를 설정하는 함수
def set_parent():
  dfs(1,0) # 루트 노드는 1번 노드
  for i in range(1, log):
    for j in range(1, n+1):
      parent[j][i] = parent[parent[j][i-1]][i-1]

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a,b):
  # b가 더 깊도록 설정
  if d[a] > d[b]:
    a,b = b,a
  # 먼저 깊이가 동일하도록
  for i in range(log-1,-1,-1):
    if d[b] - d[a] >= (1 << i):
      b = parent[b][i]
  # 부모가 같아지도록
  if a == b:
    return a
  for i in range(log-1,-1,-1):
    # 조상을 향해 거슬러 올라가기
    if parent[a][i] != parent[b][i]:
      a = parent[a][i]
      b = parent[b][i]
  # 이후에 부모가 찾고자 하는 조상
  return parent[a][0]

set_parent()
m = int(input())

for i in range(m):
  a, b = map(int,input().split())
  print(lca(a,b))
```