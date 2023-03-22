# 21735 눈덩이 굴리기
# 31256KB / 40ms

import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int,input().split()) # 10 5
snow = [0] + list(map(int,input().split())) # 1 3 4 5 6 7 8 10 12 14
maxsize = -1

def dfs(x, t, size):
    global maxsize
    if t < 0: return # 시간을 다 쓰면 return

    maxsize = max(maxsize,size) # 모든 경우에서 max값을 저장

    if x+1 <= n:
        dfs(x+1, t-1, size+snow[x+1]) # 1칸 이동, 시간 - 1, 현재 크기 + 이동한 칸의 수
    if x+2 <= n:
        dfs(x+2, t-1, size//2+snow[x+2]) # 2칸 이동, 시간 - 1, 현재 크기//2 + 이동한 칸의 수

dfs(0,m,1) # 현재 위치 0, 주어진 시간 m, 현재 눈 크기 1
print(maxsize) # 최댓값 출력