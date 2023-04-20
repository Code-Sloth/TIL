# 14891 톱니바퀴
# 34176KB / 72ms

import sys
input = sys.stdin.readline
from collections import deque

g =[deque(list(map(int,input().rstrip()))) for _ in range(4)]

k = int(input())
for _ in range(k):
    i, d = map(int,input().split())
    i -= 1
    li = [-1] * 4
    li[i] = d
    j = i
    cd = d

    while i < 3 or j > 0:
        if i < 3: # 오른쪽
            if li[i] and g[i][2] != g[i+1][-2]: # 그 전이 회전했고, 극이 다를 때
                d = -d # 방향 변환
                li[i+1] = d # 그 인덱스에 방향 저장
            else: li[i+1] = 0 # 회전하지 않았거나 극이 같으면 더이상 돌지 않도록 0을 저장
        if j > 0: # 왼쪽
            if li[j] and g[j][-2] != g[j-1][2]:
                cd = -cd
                li[j-1] = cd
            else: li[j-1] = 0
        i += 1
        j -= 1
    
    for i in range(4):
        if li[i]: # 회전할 수 있으면
            g[i].rotate(li[i]) # 저장한 방향대로 회전


print(g[0][0]*1 + g[1][0]*2 + g[2][0]*4 + g[3][0]*8) # 1일 때만 값이 생기니까 곱해줌