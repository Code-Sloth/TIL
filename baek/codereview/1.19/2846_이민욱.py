import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

t = int(input())
n = list(map(int,input().split()))

mx = []
j = 0
for i in range(t-1):
    if n[i] >= n[i+1]:
        mx.append(n[i]-n[j])
        j = i+1
    elif i == t-2 and n[i] < n[i+1]:
        mx.append(n[-1]-n[j])
print(max(mx))