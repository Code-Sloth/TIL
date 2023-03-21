# 10039 평균 점수

total = 0
for _ in range(5):
    n = int(input())
    if n < 40:
        total += 40
    else:
        total += n
print(total//5)

# 10871 X보다 작은 수

n, x = map(int,input().split())

for i in list(map(int,input().split())):
    if i < x:
        print(i,end=' ')

# 2480 주사위 세개

nums = list(map(int,input().split()))
money = 0

for i in nums:
    if nums.count(i) == 3:
        money = 10000 + i * 1000
        break
    elif nums.count(i) == 2:
        money = 1000 + i * 100
        break
    else:
        money = max(nums) * 100

print(money)

# 10886 0 = not cute / 1 = cute

cute_li = [0,0]
for _ in range(int(input())):
    cute_li[int(input())] += 1

if cute_li[0] < cute_li[1]:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')

# 2506 점수계산

total_point = 0
point = 0
n = int(input())

for i in list(map(int,input().split())):
    if i == 0:
        point = 0
    else:
        point += 1
        total_point += point
print(total_point)
