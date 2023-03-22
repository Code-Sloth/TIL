# 1926 그림

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

from collections import deque

n, m = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x,y):
    global t,max_t
    q = deque([(x,y)])
    g[x][y] = 0
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx,ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny]:
                t += 1
                g[nx][ny] = 0
                print(g)
                q.append((nx,ny))
    if t > max_t: max_t = t
    return 1

max_t,result,is_ = 0,0,0
for i in range(n):
    for j in range(m):
        if g[i][j]:
            t = 1
            result += bfs(i,j)
        else: is_ += 1
if is_ == n*m:print(0,0,sep='\n')
else: print(result,max_t,sep='\n')
