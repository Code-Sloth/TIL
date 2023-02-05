# 11강

<br/>

## 플루이드 워셜 알고리즘(Floyd Warshall)

<br/>

## 알고리즘 개요
- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
- 플로이드 워셜 알고리즘은 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행
  - 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요치 않음
- 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장
- 플로이드 워셜 알고리즘은 다이나믹 프로그래밍 유형
- 각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인
  - a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사
- 점화식
  - D_ab = min(D_ab,D_ak+ D_kb)
  - a에서 b로 가는 거리는 a->b 과 a->k + k->b의 거리값을 비교해서 최소값을 도출

<br/>

### 코드 구현
```python
INF = int(1e9)
n = int(input())
m = int(input())
g = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      g[a][b] = 0

for _ in range(m):
  a, b, c = map(int,input().split())
  g[a][b] = c

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      g[a][b] = min(g[a][b], g[a][k] + g[k][b])

for a in range(1, n+1):
  for b in range(1, n+1):
    print('INFINITY',end=' ') if g[a][b] == INF else print(g[a][b],end=' ')
  print()
```

<br/>

### 성능 분석
- 노드의 개수가 N개일 때 알고리즘상으로 N번의 단계를 수행
  - 각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐 가는 모든 경로를 고려
- 따라서 플로이드 워셜 알고리즘의 총 시간 복잡도는 O(N^3)

<br/>

# 12강

<br/>

## 벨만 포드 알고리즘

<br/>

### 음수 간선이 포함된 상황에서의 최단 거리 문제
- [BOJ 11657 타임머신](https://www.acmicpc.net/problem/11657)
- 음수 간선이 포함되더라도 다익스트라 최단 경로 알고리즘 이용가능
- 하지만 음수 간선의 순환이 포함된다면 음의 무한인 노드가 발생
  - 벨만 포드 알고리즘은 음수 간선의 순환을 감지 가능
  - 벨만 포드의 시간 복잡도는 O(VE)로 다익스트라에 비해 느림

<br/>

### 동작 원리
- 출발 노드를 설정
- 최단 거리 테이블을 초기화
- 다음의 과정을 N-1번 반복
  - 전체 간선 E개를 하나씩 확인
  - 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
- 만약 음수 간선 순황이 발생하는지 체크하고 싶다면 3번의 과정을 한 번 더 수행
  - 이 때 최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재

<br/>

### 다익스트라와 벨만 포드 비교
- 다익스트라
  - 매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
  - 음수 간선이 없다면 최적의 해를 찾을 수 있음
- 벨만 포드
  - 매번 모든 간선을 전부 확인
    - 따라서 다익스트라 알고리즘에서의 최적의 해를 항상 포함
  - 다익스트라에 비해 오래 걸리지만 음수 간선 순환을 탐지 가능

<br/>

### 코드 구현
```python
INF = int(1e9)
n, m = map(int,input().split())
edge = []
d = [INF] * (n+1)
for _ in range(m):
  a, b, c = map(int,input().split())
  edge.append((a,b,c))

def bf(st):
  d[st] = 0
  for i in range(n):
    for j in range(m):
      cur = dege[j][0]
      next_node = dege[j][1]
      cost = edge[j][2]
      if d[cur] != INF and d[next_node] > d[cur] + cost:
        d[next_node] = d[cur] + cost
        if i == n-1:
          return True
  return False

negative_cycle = bf(1)

if negative_cycle:print(-1)
else:
  for i in range(2, n+1):
    if d[i] == INF:
      print(-1)
    else:
      print(d[i])
```