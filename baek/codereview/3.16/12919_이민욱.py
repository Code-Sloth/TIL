# 12919 A 와 B 2

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

s = input().rstrip()
t = input().rstrip()
ls = len(s)
lt = len(t)

def dfs(t,lt):
    if t==s: print(1); sys.exit()
    if lt < ls: return

    if t[-1]=='A':
        dfs(t[:-1],lt-1)
    if t[0]=='B':
        dfs(t[1:][::-1],lt-1)

dfs(t,lt)
print(0)

# 시간 초과

# s = input().rstrip()
# t = input().rstrip()
# ls = len(s)
# lt = len(t)

# def dfs(s,ls):
#     if s == t: print(1); sys.exit()
#     elif ls >= lt: return
#     dfs(s + 'A',ls+1)
#     dfs((s + 'B')[::-1],ls+1)

# dfs(s,ls)
# print(0)