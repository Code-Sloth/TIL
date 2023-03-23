# 스택(stack)
- 선입 후출(Last in first out)

<br/>

### 시간 복잡도
- 데이터 추가 : O(1)
- 데이터 삭제 : O(1)
- 데이터 확인 : O(1)

<br/>

### 사용 예
- 수식의 괄호 체크
- 후위표기법(postfix notation)
- DFS (깊이 우선 탐색)

<br/>

# 큐(queue)
- 선입 선출(First in first out)

<br/>

### 시간 복잡도
- 데이터 추가 : O(1)
- 데이터 삭제 : O(1)
- 데이터 확인 : O(1)

<br/>

### 사용 예
- 프린터의 대기열
- 메세지 큐
- BFS (넓이 우선 탐색)

<br/>

### 큐 모듈
- 목록

|번호|명령어|설명|
|--|--------|----------------------------------------------------|
|1|**from queue import Queue**|Queue 모듈을 불러옴|
|2|**que = Queue(i)**|i만큼 입력제한을 두며 que에 Queue를 적용|
|3|**que.put(a)**|que에 a를 추가|
|4|**que.get()**|que의 첫 번째 요소를 반환 및 삭제|
|5|**que = LifoQueue()**|스택과 동일한 방식으로 que를 적용|
|6|**que = PriorityQueue()**|우선순위에 따른 방식으로 que를 적용|
|7|**que.put(i,a)**|우선순위 i를 기준으로 a를 추가|

<br/>

# 덱(Deque)
- 스택 + 큐

<br/>

### 시간 복잡도
- 데이터 추가 : O(1)
- 데이터 삭제 : O(1)
- 데이터 확인 : O(1)

<br/>

### 사용 예
- 회문

<br/>

### 덱 메서드 (리스트에 없는 메서드)

- 목록

|번호|명령어|설명|
|--|--------|----------------------------------------------------|
|1|**from collections import deque**|deque 모듈을 불러옴|
|2|**q = deque()**|q에 deque를 적용|
|3|**q.appendleft(a)**|a를 q의 왼쪽에 추가|
|4|**q.popleft()**|q의 가장 왼쪽 요소 반환 및 삭제|
|5|**q.extendleft(li)**|q의 왼쪽에 li를 순환하며 하나씩 추가|
|6|**q.rotate(i)**|i만큼 q를 회전(양수:시계,음수:반시계)|