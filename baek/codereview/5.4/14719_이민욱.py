# 14719 빗물
# 31256KB / 64ms

n,m = map(int,input().split())
g = list(map(int,input().split()))

t = 0
for y in range(1,n+1):              # 높이 탐색
    temp = False                    # 벽일 때
    index = 0                       # 벽의 index
    for x in range(m):              # 좌우 탐색
        if g[x] >= y:               # 벽일 때,
            if temp:                # 처음 만난 벽이 아니면
                t += x - index - 1  # 그 사이의 공간만큼 추가
            index = x               # index 저장
            temp = True             # 처음 벽을 만나면 True

print(t)