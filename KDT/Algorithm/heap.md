# 힙

<br/>

- 원소들이 항상 정렬된 상태로 추가되고 삭제됨(binary tree기반)
- 파이썬은 기본으로 최소 힙
- 추가와 삭제가 리스트O(N)보다 시간 복잡도가 작음O(logN)
- 중복 값 허용
- 튜플 추가 가능

<br/>

## 목록
|번호|명령어|설명|
|--|--------|----------------------------------------------------|
|1|**import heapq**|heap 모듈 생성|
|2|**heapq.heapify(h)**|h를 힙구조로 변환|
|3|**heap.heappush(h,a)**|h에 a요소를 추가|
|4|**heapq.heappop(h)**|h의 첫 번째 요소를 반환 후 삭제|
|5|**heapq.heappush(h,(-n,n))**|최대 힙으로 변환|


<br/>

```python
🌈 import heapq
heap 모듈을 불러옴
```

```python
🌈 heapq.heapify(h)
기존의 h리스트를 힙구조로 변환

h = [3,5,2,4,1]
print(h)
heapq.heapify(h)
print(h)
#[3, 5, 2, 4, 1]
# [1, 3, 2, 4, 5]
```

```python
🌈 heapq.heappush(h,a)
h에 a요소를 추가

h = [3,5,2,4,1]
heapq.heapify(h)
heapq.heappush(h,6)
print(h)
# [1, 3, 2, 4, 5, 6]
```

```python
🌈 heapq.heappop(h)

h = [3,5,2,4,1]
heapq.heapify(h)
heapq.heappop(h)
print(h)
# [2, 3, 5, 4]
```

```python
🌈 heapq.heappush(heap,(-n,n))
print(heapq.heappop(heap)[-1])
최대 힙으로 변환

li = [3,5,2,4,1]
h = []
for n in li:
  heapq.heappush(h,(-n,n))
while h:
  print(heapq.heappop(h)[1])
# 5
# 4
# 3
# 2
# 1
```
