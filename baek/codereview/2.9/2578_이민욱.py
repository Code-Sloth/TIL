# 2578 빙고

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

g = [list(map(int,input().split())) for _ in range(5)]
order = [list(map(int,input().split())) for _ in range(5)]
di = {}

for i in range(5):
    for j in range(5):
        di[g[i][j]] = i,j

l = [0] * 12
t = 0
for ord in order:
    for i in range(5):
        b = di[ord[i]]
        t += 1
        if b[0] == b[1]: l[0] += 1
        if b[0] + b[1] == 4: l[1] += 1
        cnt3 = -5
        for cnt1 in range(2):
            cnt3 += 5
            for cnt2 in range(5):
                if b[cnt1] == cnt2: l[cnt2+cnt3+2] += 1
        if l.count(5) > 2:
            print(t)
            exit()
