# 문제에서 주어지는 입력을 받기 적합한 입력 코드를 작성하세요.

# 입력과 동일하게 출력하는 코드를 작성하세요.

# ☁ 예제 1 ☁
# 5
n = int(input())
print(n)

# ☁ 예제 2 ☁
# 2 5
a, b = map(int,input().split())
print(a, b)

# ☁ 예제 3 ☁
# 1 2 3
nums = list(map(int,input().split()))
print(*nums)

# ☁ 예제 4 ☁
# word1 word2 word3
s = list(input().split())
print(*s)

# ☁ 예제 5 ☁
# 1 2 3 4 5
nums = list(input().split())
print(' '.join(nums))

# ☁ 예제 6 ☁
# -10 -10
a, b = map(int,input().split())
print(a, b)

# ☁ 예제 7 ☁
# 3 17 1 39 8 41 2 32 99 2
s = list(input().split())
print(*s)

# ☁ 예제 8 ☁
# 1 4 0 10 2 3 9
nums = list(map(int,input().split()))
print(*nums)

# ☁ 예제 9 ☁
nums = list(map(int,input().split()))
print(*nums)