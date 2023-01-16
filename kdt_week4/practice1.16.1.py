import sys
sys.stdin = open('input.txt','r')

# 1000 A+B

a, b = map(int,input().split())
print(a+b)

# 2558 A+B - 2

a = int(input())
b = int(input())

print(a+b)

# 10950 A+B - 3

t = int(input())

for _ in range(t):
    a, b = map(int,input().split())
    print(a+b)

# 10953 A+B - 6

t = int(input())

for _ in range(t):
    a, b = map(int,input().split(','))
    print(a+b)

# 11021 A+B - 7

t = int(input())

for _ in range(1,t+1):
    a, b = map(int,input().split())
    print(f'Case #{_}: {a+b}')

# 11022 A+B - 8

t = int(input())

for _ in range(1,t+1):
    a, b = map(int,input().split())
    print(f'Case #{_}: {a} + {b} = {a+b}')