# 1193 분수찾기

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())

i = 0 
while n > (i*(i+1))//2: 
    i += 1

subtra = (i*(i+1))//2 - n + 1
if i % 2 != 0:
    print(f'{subtra}/{i+1-subtra}')
else:
    print(f'{i+1-subtra}/{subtra}')
