# 1강

<br/>

## 스택 자료구조
- 먼저 들어온 데이터가 나중에 나가는 형식(선입 후출)의 자료구조
- 입구와 출구가 동일한 형태로 스택을 시각화 가능
- ```python
  stack = []
  stack.append(5)
  stack.append(2)
  stack.append(3)
  stack.append(7)
  stack.pop()
  stack.append(1)
  stack.append(4)
  stack.pop()

  print(stack[::-1])
  print(stack)

  # [1, 3, 2, 5]
  # [5, 2, 3, 1]
  ```

<br/>

## 큐 자료구조
- 먼저 들어온 데이터가 먼저 나가는 형식(선입 선출)의 자료구조
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태
- 단순히 list를 이용해서 구현할 수 있지만 시간적으로 효율이 떨어짐 그래서 deque이용
- ```python
  from collections import deque
  queue = deque()
  queue.append()
  queue.append()
  queue.append()
  queue.append()
  queue.popleft()
  queue.append()
  queue.append()
  queue.popleft()

  print(queue)
  queue.reverse()
  print(queue)

  # deque([3, 7, 1, 4])
  # deque([4, 1, 7, 3])
  ```

<br/>

# 2강

<br/>

## 우선순위 큐
- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- 데이터를 우선순위에 따라 처리하고 싶을 때 사용
- ex) 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야 하는 경우
- 구현하는 방법
  - 단순히 리스트를 이용해 구현
  - 힙(heap)을 이용하여 구현
- |우선 순위 큐 구현 방식|삽입 시간|삭제 시간|
  |--|--|--|
  |리스트|O(1)|O(N)|
  |힙(heap)|O(logN)|O(logN)|
- 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일(힙 정렬)
  - 이 경우 O(NlogN)

<br/>

## 힙(Heap)
- 힙은 완전 이진 트리 자료구조의 일종
- 힙에서는 항상 루트 노드(root node)를 제거
- 최소 힙(min heap)
  - 루트 노드가 가장 작은 값을 가짐
  - 따라서 값이 작은 데이터가 우선적으로 제거
- 최대 힙(max heap)
  - 루트 노드가 가장 큰 값을 가짐
  - 따라서 값이 큰 데이터가 우선적으로 제거
- 완전 이진트리
  - 루트 노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입되는 트리
- 최소 힙 구성 함수(min-heapify())
  - (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체
- 파이썬은 min-heap이 기본이라 오름차순, max-heap은 데이터를 넣을때와 꺼낼 때 -로 설정하면 됨
- ```python
  import sys
  import heapq
  input = sys.stdin.readline

  def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
      heapq.heappush(h, value)
    for i in range(len(h)):
      result.append(heapq.heappop(h))
    return result

  n = int(input())
  li = []

  for i in range(n):
    li.append(int(input()))
  
  res = heapsort(li)

  for i in range(n):
    print(res[i])
  ```

<br/>

# 3강

<br/>

## 트리
- 가계도와 같은 계층적인 구조를 표현할 때 사용할 수 있는 자료구조
- 트리 관련 용어
  - 루트 노드 : 부모가 없는 최상위 노드
  - 단말 노드 : 자식이 없는 노드
  - 크기 : 트리에 포함된 모든 노드의 개수
  - 깊이 : 루트 노드부터의 거리 (루트 노드의 깊이는 0)
  - 높이 : 깊이 중 최댓값
  - 차수 : 각 노드의 (자식 방향) 간선 개수 (자식이 몇 개인지)
- 기본적으로 트리의 크기가 N일 때, 전체 간선의 개수는 N-1

<br/>

## 이진 탐색 트리(Binary Search Tree)
- 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조
- 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드
- 루트 노드부터 값을 비교하며 오른쪽 or 왼쪽을 제외하고 다시 탐색 반복으로 효율적

<br/>

## 트리의 순회(Tree Traversal)
- 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법
  - 트리의 정보를 시각적으로 확인 가능
- 대표적인 트리 순회 방법
  - 전위 순회(pre-order traverse) : 루트를 먼저 방문 A-B-D-E-C-F-G
  - 중위 순회(in-order traverse) : 왼쪽 자식을 방문한 뒤에 루트를 방문  D-B-E-A-F-C-G
  - 후위 순회(post-order traverse) : 오른쪽 자식을 방문한 뒤에 루트를 방문  D-E-B-F-G-C-A
  - ```python
                    A
              B           C
          D      E     F      G
    ```

<br/>

# 4강

<br/>

## 구간 합 문제
- [BOJ 구간 합 구하기 문제](https://www.acmicpc.net/problem/2042)

<br/>

## 바이너스 인덱스 트리(Binary Indexed Tree)
- 2진법 인덱스 구조를 활용해 구간 합 문제를 효과적으로 해결해 줄 수 있는 자료구조(펜윅 트리(fenwick tree))
- 0이 아닌 마지막 비트를 찾는 방법
  - k & -k (6 : 00000000 00000000 00000000 00000110 : k & -k -> 2)
  - ```python
    n = 8
    for i in range(n+1):
      print(i, '의 마지막 비트:', (i & -i))
    ```
- ```python
  n,m,k = map(int,input().split())

  arr = [0] * (n+1)
  tree = [0] * (n+1)

  def prefix_sum(i):
      result = 0
      while i > 0:
          result += tree[i]
          i -= (i&-i)
      return result

  def update(i,dif):
      while i <= n:
          tree[i] += dif
          i += (i&-i)
          print(tree)

  def interval_sum(start,end):
      return prefix_sum(end) - prefix_sum(start - 1)

  for i in range(1,n+1):
      x = int(input())
      arr[i] = x
      update(i,x)
      

  for i in range(m+k):
      a,b,c = map(int,input().split())
      if a == 1:
          update(b,c-arr[b])
          arr[b] = c
      else:
          print(interval_sum(b,c))
  ```

<br/>

- ![tree1](https://raw.githubusercontent.com/Code-Sloth/TIL/master/mlp/image/tree1.png)
