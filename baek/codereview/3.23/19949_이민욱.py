# 19949 영재의 시험
# 31256KB / 2176ms

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

g = list(map(int,input().split()))
di = {i : g[i] for i in range(10)}
li = []
cnt = 0

def dfs(t,po):
    global cnt

    if t == 10:
        if po >= 5: 
            cnt += 1
        return

    for i in range(1,6):
        if t <= 1 or li[t-2] != li[t-1] or li[t-1] != i:
            li.append(i)
            if i == di[t]:
                dfs(t+1,po+1)
            else:
                dfs(t+1,po)
            li.pop()

dfs(0,0)
print(cnt)