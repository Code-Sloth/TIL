# 3190 뱀
# 34176KB / 76ms

import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
from collections import deque

n = int(input())
apple = int(input())
apple_index = set(tuple(map(int,input().split())) for _ in range(apple))

turn = int(input())
turn_i = deque([input().split() for _ in range(turn)]+[(0,0)])
d = [(-1,0),(0,1),(1,0),(0,-1)] # 상 우 하 좌 / -1이 되면 오류 발생하니 1위치에 우
snake = deque([(1,1)]) # 뱀의 모든 부위(머리,몸,꼬리) 위치를 저장

def func_turn(d,dir):
    return (d+1) % 4 if dir == 'D' else (d-1) % 4

def dfs(x,y,d_index,t):
    if x < 1 or x > n or y < 1 or y > n or (x,y) in snake:
        return t # 인덱스를 벗어나거나 몸에 부딪히면 시간을 반환

    snake.append((x,y)) # 한 칸 갈 때마다 snake에 담음
    # print(snake)

    if (x,y) not in apple_index: snake.popleft()  # 사과가 아닐 때 꼬리칸 제거
    else: apple_index.remove((x,y)) # 이미 사용한 사과의 인덱스를 제거

    if t == int(turn_i[0][0]): # 방향을 바꿀 시간에
        d_index = func_turn(d_index, turn_i[0][1]) # 방향 변환 후 저장
        turn_i.popleft() # 변환했기 때문에 리스트에서 제거
        
    return dfs(x+d[d_index][0], y+d[d_index][1], d_index, t+1)
     # 현재 방향에서 1칸 나아가고 시간도 +1
print(dfs(1,2,1,1)) # 오른쪽 1칸 이동하면서 dfs

'''
# 3190 뱀
# 34200KB / 72ms

from collections import deque

n = int(input()) # 보드 크기
apple = int(input()) # 사과 개수
g = [[0]*n for _ in range(n)] # 보드
for i in range(apple):
    a,b = map(int,input().split())
    g[a-1][b-1] = 2 # 사과를 보드에 넣어줌

turn = int(input()) # 방향 변환 횟수
turn_i = deque([input().split() for _ in range(turn)]+[(0,0)]) # 방향 변환 정보
d = [(-1,0),(0,1),(1,0),(0,-1)] # 상 우 하 좌 / -1이 되면 오류 발생하니 1위치에 우
q = deque([(0,0)]) # 첫 인덱스 저장하기 위한 덱
g[0][0] = 1 # 시작점 미리 1

def func_turn(d,dir): # 방향 변환 함수
    return (d+1) % 4 if dir == 'D' else (d-1) % 4

def dfs(x,y,d_index,t):
    if x < 0 or x >= n or y < 0 or y >= n or g[x][y] == 1:
        return t # 보드 밖으로 나가거나 몸에 부딪히면 시간을 반환

    q.append((x,y)) # 한 칸 갈 때마다 q에 담음

    if g[x][y] != 2: # 사과가 아닐 때
        a,b = q.popleft()
        g[a][b] = 0 # 꼬리칸을 없앰
    g[x][y] = 1 # 현재 칸 1로 표시

    if t == int(turn_i[0][0]): # 방향을 바꿀 시간에
        d_index = func_turn(d_index, turn_i[0][1]) # 방향 변환 후 저장
        turn_i.popleft() # 변환했기 때문에 리스트에서 제거
    return dfs(x+d[d_index][0], y+d[d_index][1], d_index, t+1)
    # 현재 방향에서 1칸 나가고 시간도 +1

print(dfs(0,1,1,1)) # 오른쪽 1칸 이동하면서 dfs
'''