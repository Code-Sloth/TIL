# 18429 근손실
# 31256KB / 104ms

import sys
input = sys.stdin.readline

from itertools import permutations

n, k = map(int,input().split())
a = list(map(int,input().split()))

result = 0

for i in permutations(a,n):
    is_500 = True
    t = 0
    for j in i:
        t = t + j - k
        if t < 0:
            is_500 = False
            break
    if is_500:
        result += 1

print(result)