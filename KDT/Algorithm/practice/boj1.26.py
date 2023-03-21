# 10101 삼각형 외우기 https://www.acmicpc.net/problem/10101

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

angle = [0] * 3
for _ in range(3):
    angle[_] = int(input())

if sum(angle) == 180:
    for i in angle:
        if angle.count(i) == 3:
            print('Equilateral')
            break
        if angle.count(i) == 2:
            print('Isosceles')
            break
    else: print('Scalene')
else:
    print('Error')

# 2720 세탁소 사장 동혁 https://www.acmicpc.net/problem/2720

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for _ in range(int(input())):
    mon = int(input())
    q = mon // 25
    d = (mon % 25) // 10
    n = (mon % 25) % 10 // 5
    p = (mon % 25 ) % 10 % 5
    print(q, d, n, p, sep = ' ')

# 1453 피시방 알바 https://www.acmicpc.net/problem/1453

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

li = [0] * 101
t = 0
for _ in range(int(input())):
    nums = list(map(int,input().split()))
    for i in nums:
        if li[i]:
            t += 1
        else:li[i] += 1
print(t)

# 10773 제로 https://www.acmicpc.net/problem/10773

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

li = []
for _ in range(int(input())):
    n = int(input())
    li.append(n) if n!=0 else li.pop()
print(sum(li))

# 2161 카드1 https://www.acmicpc.net/problem/2161

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

st = deque(range(1,int(input())+1))
while 1:
    print(st.popleft(),end = ' ')
    if st:
        st.append(st.popleft())
    else:break

# 9012 괄호 https://www.acmicpc.net/problem/9012

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    while '()' in s: s = s.replace('()','')
    print('NO') if s else print('YES')