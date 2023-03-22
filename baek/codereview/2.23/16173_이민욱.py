# 16173 점프왕 쩰리(Small)
# 31256KB / 40ms

import sys

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]

def dfs(x,y):
    if g[x][y] >= 1:
        for dx,dy in [(0,g[x][y]),(g[x][y],0)]:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if g[nx][ny] == -1:
                    print('HaruHaru')
                    sys.exit()
                else: dfs(nx,ny)
    return 'Hing'

print(dfs(0,0))