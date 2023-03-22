# 8979 올림픽

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n, k = map(int,input().split())
li = [list(map(int,input().split())) for i in range(n)]
li2 = sorted(li,key = lambda x : (x[1],x[2],x[3]),reverse = True)
t = 1

if li2[0][0] == k:print(1)
else:
    for i in range(1,len(li2)+1):
        if li2[i][1:] != li2[i-1][1:]:
            t = i+1
        if li2[i][0] == k:break
    print(t)
