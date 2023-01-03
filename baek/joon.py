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