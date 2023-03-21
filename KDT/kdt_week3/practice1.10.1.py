# ☁ 예제 1 ☁
# 정수를 출력하세요.
# 5

print(int(input()))

# ☁ 예제 2 ☁
# 단어를 구분해서 출력하세요.
# hello python world

print(*input().split())

# ☁ 예제 3 ☁
# 테스트 케이스마다 입력 값을 그대로 출력하세요.
# 3  테스트 케이스 수
# 1 
# 2 
# 3 

for i in range(1,int(input())+1):
    print(i)

# ☁ 예제 4 ☁
# 2개 이상의 정수를 출력하세요.
# 2 0 3 92 3

nums = map(int,input().split())
for i in nums:
    print(i,end=' ')

# ☁ 예제 5 ☁
# 2개의 정수를 출력하세요.
# 2 3

a, b = map(int,input().split())
print(a, b)

# ☁ 예제 6 ☁
# 단어를 구분해서 출력하세요.
# I am Programmer

s = input().split()
print(*s)

# ☁ 예제 7 ☁
# 테스트 케이스마다 입력 값을 그대로 출력하세요.
# 5 테스트 케이스 수
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# 13 14 15

t = int(input())

for i in range(t):
    nums = list(map(int,input().split()))
    for j in nums:
        print(j,end=' ')
    print()

# ☁ 예제 8 ☁
# 테스트 케이스마다 입력 값을 그대로 출력하세요.
# 5 테스트 케이스 수
# 1 38 108 29 3 2 39
# 1 9 12 3 5 1
# 28 39 1 20 9 1
# 34 5 6 8
# 9 3 2 10 1 2 4
t = int(input())

for i in range(t):
    nums = list(map(int,input().split()))
    for j in nums:
        print(j,end=' ')
    print()

