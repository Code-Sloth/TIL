# 10769 행복한지 슬픈지 https://www.acmicpc.net/problem/10769

import sys
input = sys.stdin.readline

s = input().rstrip()
s1 = s.count(':-)')
s2 = s.count(':-(')

if ':-)' not in s and ':-(' not in s: print('none')
else:
    if s1 == s2: print('unsure')
    elif s1 > s2: print('happy')
    else: print('sad')

# 2455 지능형 기차 https://www.acmicpc.net/problem/2455

import sys
input = sys.stdin.readline

t = 0
max_t = 0
for _ in range(4):
    o, i = map(int,input().split())
    t = t - o + i
    if t > max_t: max_t = t
print(max_t)

# 2606 바이러스 https://www.acmicpc.net/problem/2606
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    g[a] += [b]
    g[b] += [a]
vi = [0] * (n+1)

def dfs(x):
    vi[x] = 1
    for i in g[x]:
        if not vi[i]:
            vi[i] = 1
            dfs(i)
    return vi.count(1)-1

print(dfs(1))

# 4963 섬의 개수 https://www.acmicpc.net/problem/4963
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x,y):
    g[x][y] = 0
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:continue
        if g[nx][ny]:
            dfs(nx,ny)
    return True


while 1:
    m, n = map(int,input().split())
    if m == 0 and n == 0: break
    g = [list(map(int,input().split())) for _ in range(n)]
    d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    t = 0

    for i in range(n):
        for j in range(m):
            if g[i][j]:
                t += dfs(i,j)
    print(t)
