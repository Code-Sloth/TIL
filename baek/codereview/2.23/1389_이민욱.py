# 1389 케빈 베이컨의 6단계 법칙
# 34184KB / 72ms

from collections import deque

n, m = map(int,input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    if b not in g[a]: g[a] += [b]
    if a not in g[b]: g[b] += [a]

def bfs(x,end):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == end:
            cnt[i] += [vi[x]]
            cnt[end] += [vi[x]]
            return
        for nx in g[x]:
            if not vi[nx]:
                vi[nx] = vi[x] + 1
                q.append(nx)

cnt = [[] for _ in range(n+1)]
min_cnt = int(1e9)
for i in range(1,n+1):
    for j in range(1,n+1):
        if i < j:
            vi = [0] * (n+1)
            bfs(i,j)
    if min_cnt > sum(cnt[i]):
        min_cnt = sum(cnt[i])
        sol = i
print(sol)