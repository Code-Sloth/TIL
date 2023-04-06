# 15810 풍선 공장
# 143400KB / 1120ms

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int,input().split())
g = list(map(int,input().split()))

def binary(st, end):
    if st > end: return end+1
    mid = (st+end)//2

    result = 0
    for i in g:
        result += mid//i
    
    if result >= m:
        return binary(st, mid-1)
    else:
        return binary(mid+1, end)

print(binary(1,min(g)*m))