- 리스트 중복값 없애기 list(set(li))
- 합 구하기 li = ['123'] ==> print(sum(map(int,li[0]))) ==> # 6
```python
# 2669 직사각형 네개의 합집합의 면적 구하기 https://www.acmicpc.net/problem/2669
set_r = set()

for _ in range(4):
    r_place = list(map(int, sys.stdin.readline().split()))

    for n in range(r_place[0], r_place[2]):
        for m in range(r_place[1], r_place[3]):
            set_r.add((n,m))

print(len(set_r))
```
- range 길이가 n일 때 i%n 으로 인덱스 처음부터 접근하는 법
```python
li = [1,2,3,4,5]
n = 2
new_li = [0 for _ in range(len(li))]
for i in range(len(li)):
    new_li[(i+n)%len(li)] = li[i]
print(new_li)
```
```python
print(li[-n:] + li[:-n])
```

- rjust() 오른쪽 정렬
- statistics.mean 평균, statistics.mode 최빈값
- li[i] ^= 1 // 1은 0으로 0은 1로 바꿔줌
- 재귀함수 오류 해결 sys.setrecursionlimit(10**8)
- 반대로 순회 for i in range(n-1,-1,-1) == for i in reversed(range(n))
- 전치 쉽게 하기
```python
import numpy as np

li = [[1,2,3],
      [4,5,6],
      [7,8,9]
      ]
li2 = list(map(list,np.array(li).T))
```
```python
li = [[1,2,3],
      [4,5,6],
      [7,8,9]
      ]
      
# 전치
li2 = [list(x) for x in zip(*li)]
#[
# [1,4,7],
# [2,5,8],
# [3,6,9]
# ]

# 90도 회전
li3 = [list(x) for x in zip(*li[::-1])]
# [
#  [7,4,1],
#  [8,5,2],
#  [9,6,3]
# ]
```
- itertools combinations
- bisect.insort(li,i) li에 다른수와 비교하며 자기 자리에 삽입/다시 정렬할 필요 x
- [속도 향상 꿀Tip](https://deepwelloper.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%BD%94%EB%93%9C%EB%A5%BC-%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9C%BC%EB%A1%9C-%EC%9E%91%EC%84%B1%ED%95%98%EB%8A%94-%EB%B2%95-Part-1)
- 