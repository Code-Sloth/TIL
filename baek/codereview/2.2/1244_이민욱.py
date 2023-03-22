# 1244 스위치 켜고 끄기

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def zeroone(arr,index):
    arr[index] = 0 if arr[index] else 1

n = int(input())
li = [None] + list(map(int,input().split()))
for _ in range(int(input())):
    gender, i = map(int,input().split())
    if gender == 1:
        for k in range(i,n+1,i):
            li[k] ^= 1
    elif gender == 2:
        li[i] ^= 1
        for k in range(1,n//2+1):
            if i-k < 1 or i+k > n:break
            if li[i-k] == li[i+k]:
                li[i-k] ^= 1
                li[i+k] ^= 1
            else:break

for i in range(1,n+1):
    print(li[i],end=' ')
    if i % 20 == 0:
        print()
