# 1966 프린터 큐

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

from collections import deque

for _ in range(int(input())):
    n, m = map(int,input().split())
    li = deque(list(map(int,input().split())))
    t = 0

    while li:
        mx = max(li)
        st = li.popleft()
        m -= 1

        if st == mx:
            t += 1
            if m < 0:
                print(t)
                break
        else:
            li.append(st)
            if m < 0:
                m = len(li)-1