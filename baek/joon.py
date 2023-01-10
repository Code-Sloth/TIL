# 나름 깔끔하게 풀었던 문제들

# [Bronze III] 오븐 시계 - 2525

a,b=map(int,input().split())
c=int(input())
print((a+(b+c)//60)%24,(b+c)%60)

# [Bronze V] A+B - 3 - 10950

t=int(input())
c=[]

for i in range(t):
    a,b=map(int,input().split())
    c.append(a+b)

for i in range(t):
    print(c[i])

# [Bronze IV] 빠른 A+B - 15552

# 시간 단축을 위한 명령어

import sys
c=int(sys.stdin.readline())

for i in range(c):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)

# 못푼 문제 
# 백준 8959번 OX퀴즈

for i in range(int(input())):
    a = list(input())
    t = 0
    tot = 0
    for j in a:
        if j == 'O':
            t += 1
            tot += t
        else:
            t = 0
    print(tot)

# 못푼 문제
# 백준 1316번 그룹 단어 체크

# sol 1
n = int(input())
t = 0

for j in range(n):
    a = input() # aba
    t = 0
    for i in range(len(a)-1): # 0, 1
        if a[i] != a[i+1]:
            b = a[i+1:]
            if b.count(a[i]) > 0:
                t += 1
    if t > 0:
        n -= 1
print(n)
# sol 2
n = int(input())

result = n
cnt = 0

for i in range(n):
    str = input()
    for j in range(len(str)-1):
      
        if str[j] == str[j+1] :
            pass 
        else:
            if str[j] in str[j+1:]:
                cnt += 1
                break

print(result - cnt)

# 쓸데없이 어렵게 푼 문제
# 백준 2292번 벌집
# my sol
n = int(input())

t = 0
num = 1
if n == 1:
    num =1
else:
    while True:
        t += 1
        tt = 3*t**2-3*t+2
        if n in range(tt,3*(t+1)**2-3*(t+1)+2):
            num = t+1
            break
print(num)
# sol
n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)

# 쓸데없이 어렵게 푼 문제
# 백준 1193 분수찾기
# my sol
n = int(sys.stdin.readline())
n2 = 1
t = 0

while n > t:
    n2 += 1
    if n2 % 2 == 0:
        for i in range(1,n2):
            cnt1 = n2-i
            cnt2 = i
            t += 1
            if n == t:
                break
    else:
        for j in range(1,n2):
            cnt1 = j
            cnt2 = n2-j
            t += 1
            if n == t:
                break

print(f'{cnt1}/{cnt2}')
# sol
n = int(input())

line = 0
end = 0
while n > end:
    line += 1   # 1 2 3 4  5 
    end += line # 1 3 6 10 15

diff = end - n
if line%2 == 0: #짝수 라인 일때
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))