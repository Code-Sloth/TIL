# 2615 오목
# 31256KB / 40ms

import sys
input = sys.stdin.readline

g = [list(map(int,input().split())) for _ in range(19)]
d = [(-1,1),(1,0),(1,1),(0,1)] # 가장 왼쪽, 가장 위쪽 기준이기 때문에 우상/하/우하/우


for x in range(19):
    for y in range(19):
        if g[x][y]: # g[x][y] 값이 0이 아닐 때
            a = g[x][y] # 그 값을 a에 저장
            for dx,dy in d: # 4방향 탐색
                nx,ny = x+dx,y+dy
                t = 1 # 바둑알의 개수

                for _ in range(4): # 오목을 찾아야 하니 4번 더 반복
                    # 인덱스를 벗어나지 않고 연속된 다음 칸이 a면 바둑알의 개수 + 1
                    if 0 <= nx < 19 and 0 <= ny < 19 and g[nx][ny] == a:
                        t += 1
                    else: break

                    if t == 5: # 오목이면
                        # 육목이면 break
                        if 0 <= nx+dx < 19 and 0 <= ny+dy < 19 and g[nx+dx][ny+dy] == a:
                            break
                        # 육목이였던 곳을 두 번째 탐색할 땐 오목으로 나오기때문에 첫 바둑알 앞에 거도 생각
                        if 0 <= x-dx < 19 and 0 <= y-dy < 19 and g[x-dx][y-dy] == a:
                            break
                        print(a)
                        print(x+1,y+1)
                        sys.exit()
                    # 한 번 돌 때마다 방향에 따라 인덱스 증가
                    nx += dx
                    ny += dy
print(0)
