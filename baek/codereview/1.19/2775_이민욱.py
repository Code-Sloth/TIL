import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for _ in range(int(input())):
    floor = int(input())
    n = int(input())
    li = list(range(1,n+1))
    li2 = [0] * n
    
    for j in range(floor):
        for i in range(n):
            li2[i] = sum(li[:i+1])
        li = li2.copy()
    print(li[-1])