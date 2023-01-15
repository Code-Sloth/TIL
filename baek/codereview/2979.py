import sys
sys.stdin = open('input.txt','r')

a,b,c = map(int,input().split())
di = dict.fromkeys(range(1,101),0)

for i in range(3):
    inn,away = map(int,input().split())
    for j in range(inn,away):
        di[j] += 1
print(di)
li = list(di.values())
print(a*li.count(1) + 2*b*li.count(2) + 3*c*li.count(3))
