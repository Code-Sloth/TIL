# 16198 에너지 모으기
# 31256KB / 88ms

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
g = list(map(int,input().split()))

mx = 0
def dfs(su, ls):
    global mx

    if ls == 2:
        mx = max(mx,su)
        return

    for i in range(1,ls-1):
        mu = g[i-1] * g[i+1]
        p = g.pop(i)
        dfs(su + mu ,ls-1)
        g.insert(i,p)

dfs(0,n)
print(mx)