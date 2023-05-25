# 1138 한 줄로 서기
# 31256KB / 40ms

n = int(input())
g = list(map(int,input().split()))
index = [0] * n

for i in range(n):
    for j in range(n):
        if not g[i] and not index[j]:
            index[j] = i+1
            break
        if index[j] == 0:
            g[i] -= 1

print(*index)