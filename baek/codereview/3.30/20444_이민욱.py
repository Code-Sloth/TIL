# 20444 색종이와 가위
# 31256KB / 40ms

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, k = map(int,input().split()) # 4 6

def binary(st, end):                # 한 방향을 기준으로 자른 횟수는 0 ~ n//2
    if st > end: return 'NO'        # 이분 탐색이 끝날 때까지 못 찾으면 NO
    mid = (st+end)//2               # 이분 탐색의 중간값 설정
    paper = (mid+1)*(n-mid+1)       # 현재 조각의 개수 ((x+1) * (y+1))

    if paper == k: return 'YES'     # 현재 조각의 개수와 k가 일치하면 YES
    elif paper < k:                 # 현재 조각의 개수가 k보다 적다면
        return binary(mid+1, end)   # 시작 점을 + 1
    else:                           # 현재 조각의 개수가 k보다 많다면
        return binary(st, mid-1)    # 끝 점을 - 1

print(binary(0,n//2)) # x방향 횟수와 y방향 횟수의 차이가 최소여야 조각 개수가 최대

# x방향을 기준으로 생각, 총 1번 자른다고 하면
#   x       11  10  9   8   7   6   5   
#   y       0   1   2   3   4   5   6
#   k       12  22  30  36  40  42  42
# 중간까지 일정하게 증가 = 정렬 => 이분 탐색