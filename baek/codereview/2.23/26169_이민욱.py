# 26169 세 번 이내에 사과를 먹자
# 31256KB / 40ms

g = [list(map(int,input().split())) for _ in range(5)]
r, c = map(int,input().split())
d = [(1,0),(-1,0),(0,1),(0,-1)]
vi = [[0]*5 for _ in range(5)]

def dfs(x,y,t,apple):
    if apple == 2: print(1); exit()
    if not t: return
    vi[x][y] = 1
    for dx,dy in d:
        nx,ny = x+dx, y+dy
        if 0 <= nx < 5 and 0 <= ny < 5 and g[nx][ny] != -1 and not vi[nx][ny]:
            if g[nx][ny]:
                dfs(nx,ny,t-1,apple+1)
                vi[nx][ny] = 0
            else:
                dfs(nx,ny,t-1,apple)
                vi[nx][ny] = 0
    return 0

print(dfs(r,c,3,0))