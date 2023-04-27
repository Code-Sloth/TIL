# 11000 강의실 배정
# 73584KB / 368ms

import sys
input = sys.stdin.readline
import heapq as hq

n = int(input()) # 수업 개수
g = sorted(list(map(int,input().split())) for _ in range(n)) # 정렬된 리스트로 입력
q = [] # 수업 끝나는 시간을 모아둔 heapq

for st, end in g:
    if q and q[0] <= st: # 수업이 끝난 후에 다음 수업이 시작할 수 있으면
        hq.heappop(q)    # 수업 끝나는 시간 갱신
    hq.heappush(q, end)  # 갱신, 강의실 추가

print(len(q)) # 강의실 개수 출력

'''
ex) 입력
5
1 2
1 3
4 5
3 5
2 4

===================

g = [(1, 2),(1, 3),(2, 4),(3, 5),(4, 5)]

          st end      q[0]      q[0]

for문 1 / (1, 2)-> q = [2]
for문 2 / (1, 3)-> q = [2, 3]
for문 3 / (2, 4)-> q = [4, 3] => [3, 4]
for문 4 / (3, 5)-> q = [5, 4] => [4, 5]
for문 5 / (4, 5)-> q = [5, 5]
'''
