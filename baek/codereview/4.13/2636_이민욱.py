# 2636 치즈
# 34184KB / 88ms

from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x,y):
    q = deque([(x,y)])
    vi = [[0] * m for _ in range(n)]
    t = 0
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m: # 인덱스를 벗어나지 않으면
                if not g[nx][ny] and not vi[nx][ny]: # 공기이고, 방문한 적 없으면
                    vi[nx][ny] = 1 # 방문 처리
                    q.append((nx,ny))

                elif g[nx][ny]: # 치즈이면
                    g[nx][ny] = 0 # 녹게 함
                    vi[nx][ny] = 1 # 방문 처리
                    t += 1
    return t # 녹게 만든 칸의 수를 리턴

result = []
time = 0
while 1:
    t = bfs(0,0)
    result.append(t)
    if t == 0: break # 다 녹았을 때 멈춤
    time += 1

print(time)
print(result[-2]) # 다 녹기 1시간 전이니 result의 끝에서 2번째를 출력