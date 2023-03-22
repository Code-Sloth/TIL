# 13458 시험 감독

import sys
input = sys.stdin.readline
import math

n = int(input())
nums = list(map(int,input().split()))
b, c = map(int,input().split())
total = 0

for i in range(n):
    total += 1
    if nums[i] - b > 0:
        total += math.ceil((nums[i]-b)/c)

print(total)
