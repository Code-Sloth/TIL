# 2304 창고 다각형
# 31256KB / 40ms

mxl = mxh = 0
g = []

for _ in range(int(input())):
    l, h = map(int,input().split())
    g.append((l,h))
    if mxl < l:
        mxl = l
    if mxh < h:
        mxh = h
        mxi = l

li = [0] * (mxl + 1)
for l,h in g:
    li[l] = h

total = mxt = 0
for i in range(mxi+1):
    mxt = max(mxt, li[i])
    total += mxt

mxt = 0
for i in range(mxl, mxi, -1):
    mxt = max(mxt, li[i])
    total += mxt
    
print(total)