# 17608 막대기

li = [int(input()) for _ in range(int(input()))]
max_q = li[-1]

t = 1
for i in reversed(li):
    if i > max_q:
        max_q = i
        t += 1
print(t)

# 7568 덩치

n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]

for j in li:
    t = 1
    for k in range(n):
        if k == li.index(j):continue
        if j[0] < li[k][0] and j[1] < li[k][1]:
            t += 1
    print(t,end=' ')

# 1063 킹

def move(kx,ky,bx,by,order):
    dx,dy = d[order]
    nx,ny = kx + dx, ky + dy
    nnx,nny = nx + dx, ny + dy

    if 0 < nnx < 9 and 0 < nny < 9 and bx == nx and by == ny:
            bx,by = nnx,nny
    if 0 < nx < 9 and 0 < ny < 9:
        if nx != bx or ny != by:
            kx,ky = nx,ny
    return kx,ky,bx,by

k,b,n = input().split()
d = {'R':(1,0),'L':(-1,0),'B':(0,-1),'T':(0,1),
      'RT':(1,1),'LT':(-1,1),'RB':(1,-1),'LB':(-1,-1)}
kx,ky = ord(k[0])-64,int(k[1])
bx,by = ord(b[0])-64,int(b[1])

for i in range(int(n)):
    order = input().rstrip()
    kx,ky,bx,by = move(kx,ky,bx,by,order)

k = chr(kx+64) + str(ky)
b = chr(bx+64) + str(by)

print('\n'.join((k,b)))