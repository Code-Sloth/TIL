# 10818 최소, 최대

t = int(input())
nums = list(map(int,input().split()))
print(min(nums), max(nums))

# 11720 숫자의 합

t = int(input())
nums = list(map(int,input()))
print(sum(nums))

# 2750 수 정렬하기

t = int(input())
li = [0] * t
for i in range(t):
    li[i] = int(input())

for j in sorted(li):
    print(j)

# 2562 최댓값

nums = [0] * 9
for i in range(9):
    nums[i] = int(input())
print(max(nums), nums.index(max(nums))+1, sep = '\n')