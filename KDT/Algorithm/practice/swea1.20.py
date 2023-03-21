# 14654 신용카드 만들기 2

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    s = input()
    li = ['3','4','5','6','9']
    for i in s:
        s = s.replace('-','')
    if s[0] in li and len(s.strip()) == 16:
        is_card = True
    else:
        is_card = False
    print(f'#{t} {int(is_card)}')

# 14649 신용카드 만들기 1

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    nums = list(map(int,input().split()))
    total = 0
    for i in range(15):
        if i % 2 == 0:
            total += nums[i] * 2   
        else:
            total += nums[i]     
    n = (10 - (total % 10))%10
    print(f'#{t} {n}')

# 10804 문자열의 거울상

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    s = input()[::-1].strip()
    before = 'bdpq'
    after = 'dbqp'
    tr = str.maketrans(before,after)
    print(f'#{t} {s.translate(tr)}')

# 10505 소득 불균형

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    n = int(input())
    nums = list(map(int,input().split()))
    average = sum(nums)//n
    cnt = 0
    for i in nums:
        if i <= average:
            cnt += 1
    print(f'#{t} {cnt}')

# 3456 직사각형 길이 찾기

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    li = list(map(int,input().split()))
    for i in li:
        if li.count(i) == 1 or li.count(i) == 3:
            print(f'#{t} {i}')
            break

# 1204 1일차 - 최빈수 구하기

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline


for t in range(int(input())):
    t_c = int(input())
    max_li = 0
    li = list(map(int,input().split()))
    for i in range(101):
        if li.count(i) >= max_li:
            max_li = li.count(i)
            max_i = i
    print(f'#{t_c} {max_i}')