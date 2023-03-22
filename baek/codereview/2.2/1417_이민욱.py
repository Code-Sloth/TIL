# 1417 국회의원 선거

import sys
sys.stdin = open('./test/2_practice/1652_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
num = int(input())
li = [int(input()) for _ in range(n-1)]
if not li:print(0)
else:
    t = 0
    li.sort()
    while num <= li[-1]:
        li[-1] -= 1
        num += 1
        t += 1
        li.sort()
    print(t)