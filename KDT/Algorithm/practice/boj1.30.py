# 1225 이상한 곱셉 https://www.acmicpc.net/problem/1225

li = input().split()
print(sum(map(int,li[0]))*sum(map(int,li[1])))

# 2438 별 찍기 - 1 https://www.acmicpc.net/problem/2438

for i in range(1,int(input())+1):
    print('*'*i)

# 2739 구구단 https://www.acmicpc.net/problem/2739

n = int(input())
for i in range(1,10):
    print(f'{n} * {i} = {n*i}')

# 2953 나는 요리사다 https://www.acmicpc.net/problem/2953

li = [sum(list(map(int,input().split()))) for _ in range(5)]
print(li.index(max(li))+1,max(li))

# 2669 직사각형 네개의 합집합의 면적 구하기 https://www.acmicpc.net/problem/2669

xy = [[0] * 101 for i in range(101)]
for _ in range(4):
    li = list(map(int,input().split()))
    for x in range(li[0],li[2]):
        for y in range(li[1],li[3]):
            xy[x][y] = 1

print(sum(map(sum,xy)))