# 23304 아카라카

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

s = input().rstrip() # akbrbka

def aka(s):
    if len(s) == 1: return 1
    l = s[0:len(s)//2]
    # akb
    # a
    r = s[(len(s)+1)//2:len(s)]
    # bka
    # b
    if l != r[::-1]: return 0
    if not aka(l): return 0
    else: return 1

print('AKARAKA') if aka(s) else print('IPSELENTI')
