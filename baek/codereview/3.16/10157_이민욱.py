# 10157 자리배정
# 37876KB / 412ms

import sys
input = sys.stdin.readline

c,r = map(int,input().split())
n = int(input())
if n > r*c: print(0); sys.exit()
d = [(1,0),(0,1),(-1,0),(0,-1)]
g = [[0] * c for _ in range(r)]
g[0][0] = 1

x = y = dir = 0
for i in range(n):
    g[x][y] = 1
    x,y = x+d[dir][0], y+d[dir][1]
    if x < 0 or x >= r or y < 0 or y >= c or g[x][y]:
        x,y = x-d[dir][0], y-d[dir][1]
        dir = (dir+1) % 4
        x,y = x+d[dir][0], y+d[dir][1]

print(y-d[dir][1]+1,x-d[dir][0]+1)