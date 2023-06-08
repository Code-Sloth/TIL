# 1002 터렛
# 33376KB/44ms

import sys
input = sys.stdin.readline
import math

for _ in range(int(input())):
    li = list(map(int,input().split()))
    r_pl = li[2] + li[5]                            # 반지름의 합
    r_mi = abs(li[2]-li[5])                         # 반지름의 차
    d = math.sqrt(li[0]-li[3]**2+li[1]-li[4]**2)    # 두 원의 거리
   
    if r_mi < d < r_pl: # 서로다른 두 점
        print(2)
    elif d != 0 and r_mi == d or r_pl == d: # 내접&외접
        print(1)
    elif r_mi > d or r_pl < d or (d == 0 and li[2] != li[5]): # 안 만날 때
        print(0)
    else: 
        print(-1) # 겹칠 때