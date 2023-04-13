# 20006 랭킹전 대기열
# 31388KB / 44ms

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
g = [[] for _ in range(301)]
t = 1

for _ in range(n):
    level, nick = input().split()
    level = int(level)
    for i in range(t):
        if not len(g[i]):
            g[i].append((level,nick))
            t += 1
            break
        elif len(g[i]) < m and g[i][0][0] - 10 <= level <= g[i][0][0] + 10:
                g[i].append((level,nick))
                break

for i in g:
    if len(i) == m:
        print('Started!')
    elif len(i) > 0: print('Waiting!')
    else: break
    for j in sorted(i,key=lambda x:x[1]):
        print(*j)