# 2564 경비원
# 31256KB / 40ms / 힌트보고 품...

w, h = map(int,input().split())
n = int(input())

def dist(num, d):
    if num == 1: return 2*w + h - d     # ➡ ⬆ ⬅
    if num == 2: return d               # ➡
    if num == 3: return 2*w + h + d     # ➡ ⬆ ⬅ ⬇
    if num == 4: return w + h - d       # ➡ ⬆

g = []
for _ in range(n):
    num, d = map(int, input().split())
    g.append(dist(num, d))

dong_num, dong_d = map(int,input().split()) # 동근이 정보
dong_d = dist(dong_num, dong_d)

result = 0
for i in range(n):
    counter = abs(dong_d - g[i])        # 동근이로부터 반시계 방향 길이
    clock = 2*(w+h) - counter           # 반대 방향 길이
    result += min(counter, clock)       # 최솟값을 더해줌

print(result)