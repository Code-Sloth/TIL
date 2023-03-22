# 14247 나무자르기
# 39072KB / 92ms

n = int(input())
tree = sum(list(map(int,input().split()))) # 어차피 다 캐기때문에 합으로 담음
grow = sorted(list(map(int,input().split()))) # 제일 많이 자라는 나무를 제일 마지막에

for i in range(n):
    tree += grow[i] * i # 순서대로 자라는 수 * 지난 일 수

print(tree)