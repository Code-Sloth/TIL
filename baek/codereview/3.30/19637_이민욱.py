# 19637 IF문 좀 대신 써줘
# 44104KB / 244ms

import sys
input = sys.stdin.readline
import bisect

n, m = map(int, input().split())
name, nums = [], []

for i in range(n):
    a,b = input().split()
    name.append(a)
    nums.append(int(b))

for _ in range(m):
    i = bisect.bisect_left(nums, int(input()))
    print(name[i])


# 이분 탐색
# 60708KB / 716ms

# n,m = map(int,input().split())
# g = [input().split() for _ in range(n)]

# def binary(st, end):
#     if st > end: return end+1
#     mid = (st+end)//2
    
#     if int(g[mid][1]) >= num:
#         return binary(st, mid-1)
#     else:
#         return binary(mid+1, end)

# for _ in range(m):
#     num = int(sys.stdin.readline())
#     print(g[binary(0,n)][0])