# 14889 스타트와 링크
# 31256KB / 5052ms

import sys
input = sys.stdin.readline

from itertools import combinations

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]

mn = 10**9
for i in combinations(range(n),n//2):
    i2 = list(set(range(n)) - set(i))
    st = li = 0
    for j in combinations(i,2):
        st = st + g[j[0]][j[1]] + g[j[1]][j[0]]
    for j in combinations(i2,2):
        li = li + g[j[0]][j[1]] + g[j[1]][j[0]]

    mn = min(mn,abs(st-li))

print(mn)