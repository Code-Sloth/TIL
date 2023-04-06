# 2531 회전 초밥
# 시간초과 / pyp3는 통과

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
g = {i : int(input()) for i in range(n)}
st = result = 0

while st != n:
    li = set()
    coupon = True
    for i in range(st, st+k):
        i %= n
        li.add(g[i])
        if g[i] == c:
            coupon = False

    cnt = len(li)
    if coupon:
        cnt += 1
    result = max(result, cnt)
    st += 1

print(result)