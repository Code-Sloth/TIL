# 11856 반반

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    s = sorted(input().rstrip())
    print(f'#{t} Yes') if s[0] == s[1] and s[1] != s[2] and s[2] == s[3] else print(f'#{t} No')

# 7465 창용 마을 무리의 개수

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(x):
    vi[x] = 1
    for i in g[x]:
        if not vi[i]:
            vi[i] = 1
            dfs(i)
    return 1

for t in range(1,int(input())+1):
    n, m = map(int,input().split())
    g = [[] for _ in range(n+1)]
    vi = [0] * (n+1)
    for i in range(m):
        a, b = map(int,input().split())
        g[a] += [b]
        g[b] += [a]
    cnt = 0
    for i in range(1,n+1):
        if not vi[i]:
            cnt += dfs(i)
    print(f'#{t} {cnt}')

# 4406 모음이 보이지 않는 사람

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

li = ['a','e','i','o','u']
for t in range(1,int(input())+1):
    s = input().rstrip()
    print(f'#{t}',end=' ')
    for i in s:
        if i not in li:
            print(i,end='')
    print()

# 3499 퍼펙트 셔플

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

import math as mt

for t in range(1,int(input())+1):
    n = int(input())
    q = input().split()
    nn = mt.ceil(n/2)
    print(f'#{t}',end=' ')
    for i in range(nn):
        try:
            print(q[i],end=' ')
            print(q[i+nn],end=' ')
        except:break
    print()

# 1949 [모의 SW 역량테스트] 등산로 조성 // 실패

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x,y):
    global cnt,is_big

    for dx,dy in d:
        nx,ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and g[nx][ny] < g[x][y]:
            cnt += 1
            dfs(nx,ny)
        elif is_big == 0 and 0 <= nx < n and 0 <= ny < n and g[nx][ny] - k < g[x][y]:
            cnt += 1
            is_big += 1
            big_dfs(nx,ny,g[x][y]-1)
    is_big = 0
    if cnt > 0: cnt_li.append(cnt)
    cnt = 0

def big_dfs(x,y,z):
    global cnt
    g2 = g.copy()
    g2[x][y] = z
    for dx,dy in d:
        nx,ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and g2[nx][ny] < g2[x][y]:
            cnt += 1
            dfs(nx,ny)

d = [(1,0),(-1,0),(0,1),(0,-1)]
for t in range(1,int(input())+1):
    n, k = map(int,input().split())
    g = [list(map(int,input().split())) for _ in range(n)]
    max_g = max(map(max,g))
    cnt = 0
    is_big = 0
    cnt_li = []
    for i in range(n):
        for j in range(n):
            if g[i][j] == max_g:
                dfs(i,j)
    print(max(cnt_li) + 1)

# 1208 [S/W 문제해결 기본] 1일차 - Flatten

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# heap 풀이
import heapq as hq

for t in range(1,11):
    n = int(input())
    min_h = list(map(int,input().split()))
    max_h = []
    for i in range(100):
        hq.heappush(max_h,(-min_h[i],min_h[i]))
    hq.heapify(min_h)
    for i in range(n):
        hq.heappush(min_h,hq.heappop(min_h)+1)
        a, b = hq.heappop(max_h)
        hq.heappush(max_h,(a+1,b-1))
    print(f'#{t} {max_h[0][1]-min_h[0]}')

# list 풀이

for t in range(1,11):
    n = int(input())
    g = sorted(list(map(int,input().split())))
    while n > 0:
        g[0] += 1
        g[-1] -= 1
        g.sort()
        n -= 1
    print(f'#{t} {g[-1] - g[0]}')