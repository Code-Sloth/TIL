# 2029. 몫과 나머지 출력하기

for i in range(1,int(input())+1):
    a, b = map(int,input().split())
    print(f'#{i}',a // b, a % b)

# 2071. 평균값 구하기

t = int(input())

for i in range(1,t+1):
    nums = list(map(int,input().split()))
    print(f'#{i} {round(sum(nums)/len(nums)):.0f}')

# 1938. 아주 간단한 계산기

a, b = map(int,input().split())

print(a+b,a-b,a*b,int(a/b),sep = '\n')

# 2046. 스탬프 찍기

for i in range(int(input())):
    print('#',end='')

# 2068. 최대수 구하기

for t in range(1,int(input())+1):
    nums = list(map(int,input().split()))
    print(f'#{t}',max(nums))