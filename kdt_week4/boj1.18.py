# 9498 시험 성적

po = int(input())

if po >= 90:
    print('A')
elif po >= 80:
    print('B')
elif po >= 70:
    print('C')
elif po >= 60:
    print('D')
else:
    print('F')

# 9093 단어 뒤집기

for _ in range(int(input())):
    s = input().split()
    for i in s:
        print(i[::-1],end=' ')
    print()

# 11721 열 개씩 끊어 출력하기

n = input()

for i in range(len(n) // 10 + 1):
    print(n[10 * i : 10 * i + 10])

# 2947 나무 조각

nums = list(map(int,input().split()))

while nums != sorted(nums):
    for i in range(4):
        if nums[i] > nums[i+1]:
            nums.insert(i,nums[i+1])
            del nums[i+2]
            print(*nums)