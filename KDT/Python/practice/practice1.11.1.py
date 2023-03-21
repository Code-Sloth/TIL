# ☁ 예제 1 ☁
# 공백으로 구분된 정수

import sys
sys.stdin = open('input.txt','r')

print(*list(map(int,input().split())))

# ☁ 예제 2 ☁
# 공백으로 구분된 문자열

import sys
sys.stdin = open('input.txt','r')

s = list(input().split())

for i in s:
    print(i,end=' ')

# ☁ 예제 3 ☁
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

import sys
sys.stdin = open('input.txt','r')

t = int(input())

for i in range(1,t+1):
    n = int(input())
    for j in range(1,n+1):
        print(int(input()))

# ☁ 예제 4 ☁
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

import sys
sys.stdin = open('input.txt','r')

t = int(input())

for i in range(1,t+1):
    n = int(input())
    for j in range(1,n+1):
        n2, n3 = map(int,input().split())
        print(n2, n3)

# ☁ 예제 5 ☁
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 각 문장에 포함된 단어를 공백을 기준으로 출력하세요.

import sys
sys.stdin = open('input.txt','r')

t = int(input())

for i in range(1,t+1):
    n = int(input())
    for j in range(1,n+1):
        print(input())

# ☁ 예제 6 ☁
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

import sys
sys.stdin = open('input.txt','r')

t = int(input())

for i in range(1,t+1):
    n = int(input())
    for j in range(1,n+1):
        nums = list(map(int,input().split()))
        for k in nums:
            print(k,end=' ')
        print()

# ☁ 예제 7 ☁
# 테스트 케이스와 입력 줄 수가 같은 줄에 주어지는 경우

import sys
sys.stdin = open('input.txt','r')

t, n = map(int,input().split())

for i in range(1,t+1):
    for j in range(1,n+1):
        print(int(input()))

# ☁ 예제 8 ☁
# 테스트 케이스와 입력 줄 수가 같은 줄에 주어지는 경우

import sys
sys.stdin = open('input.txt','r')

t, n = map(int,input().split())

for i in range(1,t+1):
    for j in range(1,n+1):
        a,b = map(int,input().split())
        print(a,b)

# ☁ 예제 9 ☁
# 테스트 케이스와 입력 줄 수가 같은 줄에 주어지는 경우

import sys
sys.stdin = open('input.txt','r')

t, n = map(int,input().split())

for i in range(1,t+1):
    for j in range(1,n+1):
        nums = list(map(int,input().split()))
        for k in nums:
            print(k,end=' ')
        print()