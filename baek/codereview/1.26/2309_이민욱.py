# 2309 일곱 난쟁이

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

nums = [0] * 9
for i in range(9):
    nums[i] = int(input())
    
nums.sort()
sum_nums = sum(nums)-100

for i in range(8):
    for j in range(i+1,9):
        if sum_nums == nums[i] + nums[j]:
            for k in nums:
                if k != nums[i] and k != nums[j]:
                    print(k)
            exit()