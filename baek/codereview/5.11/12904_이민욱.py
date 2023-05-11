# 12904 A와 B
# 31380KB / 56ms

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
ls = len(s)
lt = len(t)

def dfs(t,lt):
    if t==s: print(1); sys.exit()   # 문자열이 일치하면 1 출력
    if lt < ls: return              # s의 길이보다 t의 길이가 작으면 중지

    if t[-1]=='A':                  # 문자열 마지막이 A면
        dfs(t[:-1],lt-1)            # 마지막을 제외하고 재귀
    if t[-1]=='B':                  # 문자열 마지막이 B면
        dfs(t[:-1][::-1],lt-1)      # 마지막을 제외하고 뒤집어서 재귀

dfs(t,lt)
print(0)                            # 다 돌아도 안되면 0 출력