# 2468 안전 영역
# 34184KB / 656ms

from collections import deque

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x,y,height):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not vi[nx][ny] and g[nx][ny] > height:
                vi[nx][ny] = 1
                q.append((nx,ny))
    return 1

if min(map(min,g)) == max(map(max,g)): print(1); exit()

max_t = 0
for h in range(min(map(min,g)),max(map(max,g))):
    t = 0
    vi = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j] > h and not vi[i][j]:
                t += bfs(i,j,h)
    max_t = max(max_t,t)
print(max_t)