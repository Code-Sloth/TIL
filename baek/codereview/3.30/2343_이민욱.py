# 2343 기타 레슨
# 42340KB / 316ms

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int,input().split())
g = list(map(int,input().split()))

def binary(st,end):
    if st > end: return st
    mid = (st+end)//2
    sum_g = 0
    t = m

    for i in range(n):
        if sum_g + g[i] <= mid:
            sum_g += g[i]
        else: 
            t -= 1
            sum_g = g[i]
        if not t: break
    
    if not t:
        return binary(mid+1, end)
    else:
        return binary(st, mid-1)

print(binary(max(g),sum(g)))