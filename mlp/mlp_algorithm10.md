# 다익스트라 알고리즘(Dijkstra)

<br/>

## 최단 경로 문제
- 가장 짧은 경로를 찾은 알고리즘
- 다양한 문제 상황
  - 한 지점에서 다른 한 지점까지의 최단 경로
  - 한 지점에서 다른 모든 지점까지의 최단 경로
  - 모든 지점에서 다른 모든 지점까지의 최단 경로
- 각 지점은 그래프에서 노드로 표현
- 지점 간 연결된 도로는 그래프에서 간선으로 표현

<br/>

## 다익스트라 최단 경로 알고리즘 개요
- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산
- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작
  - 현실 세계의 도로(간선)은 음의 간선으로 표현되지 않음
- 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류
  - 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복

<br/>

### 동작 과정
1. 출발 노드를 설정
2. 최단 거리 테이블을 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 3번과 4번을 반복
- 알고리즘 동작 과정에서 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가지고 있음
- 처리 과정에서 더 짧은 경로를 찾으면 새로 갱신

<br/>

### 특징
- 그리디 알고리즘 : 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복
- 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않음
  - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있음
- 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보를 저장
  - 완벽한 형태의 최단 경로를 구하려면 소스코드에 기능 추가
- 단계마다 방문하지 않은 노드 중에서 최단 거리가 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인

<br/>

### 코드 구현
```python
INF = int(1e9)
n, m = map(int,input().split())
start = int(input())
g = [[] for i in range(n+1)]
vi = [False] * (n+1)
dis = [INF] * (n+1)

for _ in range(m):
  a,b,c = map(int,input().split())
  g[a].append((b,c))

def small_node():
  min_ = INF
  index = 0
  for i in range(1, n+1):
    if dis[i] < min_ and not vi[i]:
      min_ = dis[i]
      index = i
  return index

def dijkstra(st):
  dis[st] = 0
  vi[st] = True
  for j in g[st]:
    dis[j[0]] = j[1]
  for i in range(n-1):
    now = small_node()
    vi[now] = True
    for j in g[now]:
      cost = dis[now] + j[1]
      if cost < dis[j[0]]:
        dis[j[0]] = cost
  
dijkstra(st)

for i in range(1, n+1):
  if dis[i] == INF:
    print('INFINITY')
  else: print(dis[i])
```

<br/>

### 간단한 구현 방법 성능 분석
- 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색
- 전체 시간복잡도 O(V^2)
- 일반적으로 코딩 테스트의 최단 경로 문제에서 전체 노드 개수가 5,000개 이하이면 이 코드로 해결 가능
- 하지만 노드 개수가 10,000개 이상이라면?

<br/>

## 우선순위 큐(Priority Queue)
- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- 예를 들어 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우에 우선순위 큐를 이용 가능
- Python, C++, Java를 포함한 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원

<br/>

### 힙(Heap)
- 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나
- 최소 힙, 최대 힙
- 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용

<br/>

### 다익스트라 알고리즘 개선된 구현 방법
- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙 자료구조를 이용
- 다익스트라 알고리즘 동작 기본 원리는 동일
  - 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용
  - 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 이용

<br/>

### 힙을 이용한 다익스트라 코드 구현
```python
import heapq as hq

INF = int(1e9)
n, m = map(int,input().split())
st = int(input())
g = [[] for _ in range(n+1)]
dis = [INF] * (n+1)
for _ in range(m):
  a, b, c = map(int,input().split())
  g[a].append((b,c))

def dijkstra(st):
  q = []
  hq.heappush(q, (0, st))
  dis[st] = 0
  while q:
    d, now = hq.heappop(q)
    if dis[now] < d:continue
    for i in g[now]:
      cost = d + i[1]
      if cost < dis[i[0]]:
        dis[i[0]] = cost
        hq.heappush(q,(cost, i[0]))

dijkstra(st)
for i in range(1, n+1):
  print('INFINITY') if dis[i] == INF else print(dis[i])
```

<br/>

### 개선된 구현 방법 성능 분석
- 힙 자료구조를 이용하는 다익스트라 알고리즘 시간 복잡도는 O(ElogV)
- 노드를 하나씩 꺼내 검사하는 반복문(While)은 노드의 개수 V이상의 횟수로는 처리되지 않음
  - 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연겨로딘 다른 노드들을 확인하는 총 횟수는 최대 간선개수(E)만큼 연산이 수행될 수 있음
- 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사
  - 시간 복잡도를 O(ElogE)로 판단 가능
  - 중복 간선을 포함하지 않는 경우에 이를 O(ElogV)로 정리 가능
    - O(ElogE) -> O(ElogV^2) -> O(2ElogV) -> O(ElogV)

