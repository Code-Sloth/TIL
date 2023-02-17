# 이진 탐색

<br/>

## 이진 탐색 알고리즘
- 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
- 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
  - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정
```python
[0,2,4,6,8,10,12,14,16,18]
# 중간점에서 오른쪽은 더 크기때문에 제외
[0,2,4,6]
# 중간점 2에서 왼쪽부분 제외
[4,6]
# 중간점 4 탐색 완료
[4]
```

<br/>

### 이진 탐색의 시간 복잡도
- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log_2-N에 비례
- 예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개가량의 데이터만 남음
  - 2단계를 거치면 8
  - 3단계를 거치면 4
- 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)을 보장


<br/>

### 이진 탐색 코드
```python
def binary_search(arr, target, st, end):
  if st > end: return None
  mid = (st+end) // 2
  if arr[mid] == target:
    return mid
  elif arr[mid] > target:
    return binary_search(arr,target,st,mid-1)
  else:
    return binary_search(arr,target,mid+1,end)

n, target = list(map(int,input().split()))
arr = list(map(int,input().split()))

result = binary_search(arr,target,0,n-1)
if result == None:
  print('X')
else:
  print(result+1)
# 10 7
# 1 3 5 7 9 11 13 15 17 19 입력
# 4 출력
```

<br/>

### 파이썬 이진 탐색 라이브러리
- bisect_left(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
```python
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4
print(bisect_left(a,x))
print(bisect_right(a,x))
# 2
# 4
```

<br/>

### 값이 특정 범위에 속하는 데이터 개수 구하기
```python
from bisect import bisect_left, bisect_right

def cnt(a, l, r):
  r_index = bisect_right(a,r)
  l_index = bisect_left(a,l)
  return r_index - l_index

a = [1,2,3,3,3,3,4,4,8,9]
print(cnt(a,4,4))
print(cnt(a,-1,3))
# 2
# 6
```

<br/>

### 파라메트릭 서치(Parametric Search)
- 최적화 문제를 결정문제(예 or 아니오)로 바꾸어 해결하는 기법
  - ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결
- 이코테 떡볶이 떡 만들기 문제
- 이코테 정렬된 배열에서 특정 수의 개수 구하기 문제
