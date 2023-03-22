import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

m = int(input())
n = int(input())
li = []

for i in range(m,n+1):
    t = 0
    for j in range(1,i):
        if i % j == 0:
            t += 1
            if t > 1: break
    if t == 1:
        li.append(i)
if len(li) == 0:
    print(-1)
else:
    print(sum(li),li[0],sep='\n')