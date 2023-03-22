# 11866 요세푸스 문제 0

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
li = [0] * n
li_q = [0] * n
q = deque(range(1,n+1))

for j in range(n):
    q.rotate(-(k-1))
    li_q[j] = str(q.popleft())

print(f'<{", ".join(li_q)}>')