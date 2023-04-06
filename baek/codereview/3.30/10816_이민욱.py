# 10816 숫자 카드 2
# 133172KB / 748ms

import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
ng = Counter(list(map(int,input().split())))
m = int(input())
mg = list(map(int,input().split()))

result = []
for i in mg:
    result.append(ng[i])

print(*result)


# 이분 탐색 시간 초과

# n = int(input())
# ng = sorted(list(map(int,input().split())))
# m = int(input())
# mg = list(map(int,input().split()))

# def binary(st,end):
#     if st > end: return 0
#     mid = (st+end)//2
#     ng_m = ng[mid]

#     if ng_m == i:
#         return ng[st:end+1].count(ng_m)
#     elif ng_m > i:
#         return binary(st, mid-1)
#     else:
#         return binary(mid+1, end)

# result = []
# for i in mg:
#     result.append(binary(0,n-1))

print(*result)
