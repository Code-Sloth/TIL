# 2477 참외밭
# 실패

k = int(input())
dd,rr = [],[]
g = [[0]*20 for _ in range(20)]
x,y = 9,9
g[x][y] = 1
direction = [0,(0,1),(0,-1),(1,0),(-1,0)]

for _ in range(6):
    d, r = map(int,input().split())
    dd.append(d)
    # [4, 2, 3, 1, 3, 1]
    rr.append(r)
    # [50, 160, 30, 60, 20, 100]

rr2 = sorted(rr)
di_rr = {rr2[i] : i+2 for i in range(len(rr2))}
# {20: 2, 30: 3, 50: 4, 60: 5, 100: 6, 160: 7}
di_dd = {i : direction[i] for i in dd}
# {4: (-1, 0), 2: (0, -1), 3: (1, 0), 1: (0, 1)}

index_i,index_j = [],[]
for i in range(6):
    dx,dy = di_dd[dd[i]][0],di_dd[dd[i]][1]
    index_i.append(x)
    index_j.append(y)
    for j in range(di_rr[rr[i]]-1):
        x, y = x+dx, y+dy
        g[x][y] = 1
        if g[x+dx][y+dy]:
            break
print(index_i)

# for i in g:
#     print(i,end='\n')