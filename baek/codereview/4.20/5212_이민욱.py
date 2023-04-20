# 5212 지구 온난화
# 31256KB / 44ms

import sys
input = sys.stdin.readline

r,c = map(int,input().split())
g = [list(input().rstrip()) for _ in range(r)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
se = set()
index = set()

for x in range(r):
    for y in range(c):
        if g[x][y] == 'X': # 땅이면
            index.add((x,y)) # 처음 땅이였던 위치들 저장
            t = 0
            for dx,dy in d: # 4방향 탐색
                if 0 <= x+dx < r and 0 <= y+dy < c:
                    if g[x+dx][y+dy] == '.': # 바다면
                        t += 1 # 카운트 +1
                else: t += 1 # 인덱스를 벗어나도 바다니까 카운트 +1
            if t >= 3:
                se.add((x,y)) # 없어져야 할 땅 위치들 저장
                
for x,y in se: 
    g[x][y] = '.' # 없어져야 할 땅들 바다로 바꿈
    if (x,y) in index:
        index.remove((x,y)) # 처음 땅의 위치들에서 없어져야 할 땅 위치들을 제거

x = sorted(index, key=lambda x:x[0]) # i방향 정렬 리스트
y = sorted(index, key=lambda x:x[1]) # j방향 정렬 리스트

for i in range(r):
    if x[0][0] <= i <= x[-1][0]: # i방향의 최솟값부터 최댓값사이인 인덱스들만 통과
        print(''.join(g[i][y[0][1]:y[-1][1]+1])) 
        # j방향의 최솟값부터 최댓값까지 슬라이싱해서 출력