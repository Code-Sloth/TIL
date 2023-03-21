# 2525 오븐 시계 https://www.acmicpc.net/problem/2525

a,b = map(int,input().split())
c = int(input())

print((a+(b+c)//60)%24,(b+c)%60)

# 2798 블랙잭 https://www.acmicpc.net/problem/2798

n, m = map(int,input().split())
nums = sorted(list(map(int,input().split())), reverse = True)

m_n = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sol = nums[i] + nums[j] + nums[k]
            if sol <= m:
                if m_n < sol: m_n = sol
                break
print(m_n)

# 9076 점수 집계 https://www.acmicpc.net/problem/9076

for _ in range(int(input())):
    li = sorted(list(map(int,input().split())))
    print(sum(li[1:4]) if li[3]-li[1] < 4 else 'KIN')

# 1526 가장 큰 금민수 https://www.acmicpc.net/problem/1526

for i in range(int(input()),3,-1):
    if not str(i).strip('47'):
        print(i)
        break

# 1436 영화 감독 숌 https://www.acmicpc.net/problem/1436

n = 666 
i = 1
num = int(input())
while 1:
    if '666' in str(n):
        if num == i:
            print(n)
            break
        i += 1
    n += 1