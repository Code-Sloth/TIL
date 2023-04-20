# 16918 봄버맨
# 35988KB / 1676ms

import sys
input = sys.stdin.readline

r,c,n = map(int,input().split())
g = [list(input().rstrip()) for _ in range(r)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
n -= 1 # 처음 1초는 가만있음

def func1(): # 폭탄 위치 저장
    for i in range(r):
        for j in range(c):
            if g[i][j] == 'O':
                se.add((i,j))

def func2(): # 모든 칸 폭탄
    g = [['O']*c for _ in range(r)]
    return g

def func3(): # 저장한 폭탄 위치를 이용해 그 칸과 주변 4방향 폭파
    for x,y in se:
        g[x][y] = '.'
        for dx,dy in d:
            if 0 <= x+dx < r and 0 <= y+dy < c:
                g[x+dx][y+dy] = '.'

while 1:
    se = set()
    
    func1()
    if not n: break

    g = func2()
    n -= 1
    if not n: break

    func3()
    n -= 1
    if not n: break

for i in g:
    print(''.join(i))

# 16918 봄버맨
# 35988KB / 3292ms / 함수가 훨씬 빠르다..

# import sys
# input = sys.stdin.readline

# r,c,n = map(int,input().split())
# g = [list(input().rstrip()) for _ in range(r)]
# d = [(1,0),(-1,0),(0,1),(0,-1)]
# n -= 1

# while 1:
#     se = set()
    
#     for i in range(r):
#         for j in range(c):
#             if g[i][j] == 'O':
#                 se.add((i,j))
#     if not n: break

#     g = [['O']*c for _ in range(r)]
#     n -= 1
#     if not n: break

#     for x,y in se:
#         g[x][y] = '.'
#         for dx,dy in d:
#             if 0 <= x+dx < r and 0 <= y+dy < c:
#                 g[x+dx][y+dy] = '.'
#     n -= 1
#     if not n: break

# for i in g:
#     print(''.join(i))