# 17086 아기 상어 2

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split()) # 5 4
g = [list(map(int,input().split())) for _ in range(n)] # [[0,0,1,0],[0,0,0,0],....]
d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)] # 8방향 델타 탐색 리스트

def bfs():
    q = deque([])

    for i in range(n):
        for j in range(m):
            if g[i][j]: q.append((i,j))
    # deque([(0, 2), (2, 0), (4, 3)])

    while q:
        x,y = q.popleft() # (0, 2)
        for dx,dy in d:
            nx, ny = x + dx, y + dy # (1, 2)
            if 0 <= nx < n and 0 <= ny < m and not g[nx][ny]:
                g[nx][ny] = g[x][y] + 1
                q.append((nx,ny)) # deque([(2, 0), (4, 3) , (1, 2)])
                for i in g:
                    print(i,end='\n')
                print()
    return max(map(max,g))

print(bfs()-1)