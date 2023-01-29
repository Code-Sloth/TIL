# 5강

<br/>

## 정렬 알고리즘
- 정렬(Sorting)이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말함
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용

<br/>

## 선택 정렬
- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞의 데이터와 바꾸는 것을 반복
- 시간 복잡도 O(N^2)
```python
li = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(li)):
  min_i = i
  for j in range(i+1, len(li)):
    if li[min_i] > li[j]:
      min_i = j
  li[i], li[min_i] = li[min_i], li[i]
print(li)
# [0,1,2,3,4,5,6,7,8,9]
```

<br/>

## 삽입 정렬
- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작
- 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
- 최선의 경우 시간 복잡도 O(N)
- 시간 복잡도 O(N^2)
```python
li = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(li)):
  for j in range(i, 0, -1):
    if li[j] < li[j-1]:
      li[j],li[j-1] = li[j-1],li[j]
    else:
      break
print(li)
# [0,1,2,3,4,5,6,7,8,9]
```

<br/>

# 6강

<br/>

## 퀵 정렬
- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
- 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정
- 시간 복잡도 O(NlogN) 최악의 경우는 O(N^2)

```python
5 7 9 0 3 1 6 2 4 8
# 피벗은 5로 정하고 왼쪽에서부터 5보타 큰 데이터 선택
# 오른쪽에서부터 5보다 작은 데이터 선택 후 교환 반복
# 위치가 엇갈리는 경우 피벗과 작은 데이터를 서로 변경
# 이제 피벗을 기준으로 왼쪽과 오른쪽으로 분할(Divide)
# 반복
```

```python
li = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(li, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    while left <= end and li[left] <= li[pivot]:
      left += 1
    while right > start and li[right] >= li[pivot]:
      right -= 1
    if left > right:
      li[right], li[pivot] = li[pivot], li[right]
    else:
      li[left], li[right] = li[right], li[left]
    quick_sort(li, start, right-1)
    quick_sort(li, right+1, end)

quick_sort(li, 0, len(li)-1)
print(li)
# [0,1,2,3,4,5,6,7,8,9]
```

```python
# 위 코드보다 파이썬의 장점을 살린 간결한 방식
li = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(li):
  if len(li) <= 1:
    return li
  pivot = li[0]
  tail = li[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(li))
# [0,1,2,3,4,5,6,7,8,9]
```

<br/>

## 계수 정렬
- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
- 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N+K) 보장
- 공간 복잡도 또한 O(N+K)
- 때에 따라서 심각한 비효율성 초래 ex) 0과 999,999만 있을 때
- 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용
  - 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적

```python
li = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(li) + 1)

for i in range(len(li)):
  count[li[i]] += 1
for i in range(len(count)):
  for j in range(count[i]):
    print(i,end=' ')
# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
```

<br/>

# 7강

<br/>

## 정렬 알고리즘 비교
- 추가적으로 대부분의 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리(sort)는 최악의 경우에도 O(NlogN)을 보장
- 선택 정렬보다 기본 정렬 라이브러리가 훨씬 빠름

|정렬 알고리즘|평균 시간 복잡도|공간 복잡도|특징|
|--|--|--|--|
|**선택 정렬**|O(N^2)|O(N)|아이디어가 매우 간단|
|**삽입 정렬**|O(N^2)|O(N)|데이터가 거의 정렬되어 있을 때 가장 빠름|
|**퀵 정렬**|O(NlogN)|O(N)|대부분의 경우에 가장 적합, 충분히 빠름|
|**계수 정렬**|O(N+K)|O(N+K)|데이터의 크기가 한정되어 있는 경우만 사용,매우 빠름|

```python
n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:break

print(sum(a))
```