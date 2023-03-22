# 14888 연산자 끼워넣기
# 31256KB / 60ms

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
pl, mi, mu, di = list(map(int,input().split()))
mx, mn = -10**10, 10**10

def dfs(pl, mi, mu, di, cnt, t):
    global mx, mn

    if cnt >= n:
        mx = max(mx,t)
        mn = min(mn,t)
        return

    if pl: dfs(pl-1, mi, mu, di, cnt+1, t + a[cnt])
    if mi: dfs(pl, mi-1, mu, di, cnt+1, t - a[cnt])
    if mu: dfs(pl, mi, mu-1, di, cnt+1, t * a[cnt])
    if di:
        if t < 0:
            dfs(pl, mi, mu, di-1, cnt+1, -(-t // a[cnt]))
        else:
            dfs(pl, mi, mu, di-1, cnt+1, t // a[cnt])

dfs(pl, mi, mu, di, 1, a[0])
print(mx,mn,sep='\n')