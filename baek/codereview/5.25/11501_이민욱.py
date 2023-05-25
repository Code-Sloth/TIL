# 11501 주식
# 173012KB / 3172ms

n = int(input())

for i in range(n):
    day = int(input())
    g = list(map(int,input().split()))[::-1]
    t, mx = 0, 0

    for i in range(len(g)):
        if g[i] > mx:
            mx = g[i]
        else:
            t += mx - g[i]

    print(t)
