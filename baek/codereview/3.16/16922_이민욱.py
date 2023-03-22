# 16922 로마 숫자 만들기
# 31256KB / 44ms

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from itertools import combinations_with_replacement

g = [1,5,10,50] # I, V, X, L
se = set()
n = int(input()) # 2
t = 0

for i in combinations_with_replacement(g,n):
    # print(i)
    su = sum(i)
    if su not in se:
        se.add(su)
        t += 1

print(t)