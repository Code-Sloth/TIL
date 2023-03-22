# 1316 그룹 단어 체커

import sys
input = sys.stdin.readline

n = int(input())

for j in range(n):
    s = input().rstrip()
    t = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if s[i+1:].count(s[i]) > 0:
                t += 1
    if t > 0: n -= 1
print(n)