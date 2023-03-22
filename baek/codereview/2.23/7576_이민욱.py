# 7576 토마토
# 98556KB / 1136ms

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

from collections import deque

def bfs():
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                q.append((i,j)) # 익은 토마토를 미리 q에 넣음
    if not q: print(-1); sys.exit() # 익은 토마토가 없을 때 -1출력
    while q:
        x, y = q.popleft()
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
                g[nx][ny] = g[x][y] + 1 
                q.append((nx,ny))
                # for i in g: print(i)
                # print()

m, n = map(int,input().split()) # 6 4
g = [list(map(int,input().split())) for _ in range(n)] # 토마토
q = deque()
d = [(1,0),(-1,0),(0,1),(0,-1)] # 4방향 델타 탐색
           
bfs() # bfs 실행

max_g = -2
for i in range(n):
    for j in range(m):
        if g[i][j] == 0: print(-1); sys.exit() # 안익은 토마토 1개라도 있으면 -1출력
        elif g[i][j] > max_g: max_g = g[i][j] # 2차원 배열의 최댓값

print(max_g-1) # 최댓값-1 = 총 걸린 최소 일 수