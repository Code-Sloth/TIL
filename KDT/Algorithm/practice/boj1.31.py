# 2441 별 찍기 - 4 https://www.acmicpc.net/problem/2441

n = int(input())
for i in range(n):
    print(' '*i,'*'*(n-i),sep='')

# 2592 대표값 https://www.acmicpc.net/problem/2592

from collections import Counter

li = [int(input()) for _ in range(10)]
print(sum(li)//10,Counter(li).most_common(1)[0][0],sep='\n')

# 10798 세로 읽기 https://www.acmicpc.net/problem/10798

li = [list(input().strip()) for i in range(5)]

for i in range(15):
    for j in range(5):
        try:
            print(li[j][i],end='')
        except:pass

# 9455 박스 https://www.acmicpc.net/problem/9455

for _ in range(int(input())):
    m, n = map(int,input().split())
    li = [list(map(int,input().split())) for __ in range(m)]
    li2 = [[0]*m for __ in range(n)]

    for i in range(m):
        for j in range(n):
            li2[j][i] = li[i][j]
    t = 0

    for i in li2:
        index = 0
        while i.count(1) > i[-i.count(1):].count(1):
            if i[index] and not i[index+1]:
                i[index],i[index+1] = 0,1
                t += 1
            index += 1
            index %= m-1
    print(t)

# sol

t=int(input())

for i in range(t):
    result=0
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(n)]
    
    for x in range(m):
        for y in range(n):
            
            if arr[y][x]==1:
                
                for z in range(y,n):
                    
                    if arr[z][x]==0:
                        result+=1
                
    print(result)

# 1652 누울 자리를 찾아라 https://www.acmicpc.net/problem/1652

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
li = [list(input().strip()) for _ in range(n)]
li2 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        li2[i][j] = li[j][i]

for i in range(n):
    li[i] = ''.join(li[i])
    li2[i] = ''.join(li2[i])

x,y = 0,0
for i in range(n):
    for j in li[i].split('X'):
        if '..' in j: x += 1
    for j in li2[i].split('X'):
        if '..' in j: y += 1
print(x,y)