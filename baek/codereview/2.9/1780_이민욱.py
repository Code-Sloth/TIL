# 1780 종이의 개수

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
g = []
for i in range(n):
    g += list(map(int,input().split()))

def nine(n,arr):
    global t_1,t1,t0
    if set(arr) == {-1}: t_1 += 1
    elif set(arr) == {0}: t0 += 1
    elif set(arr) == {1}: t1 += 1
    else:
        arr2 = []
        for i in range(n):
            arr2.append(arr[i*n:i*n+n])
        arr = arr2
        n //= 3
        if n == 0: return False
        for i1 in range(0,3*n,n):
            for i2 in range(0,3*n,n):
                new_array = []
                for i3 in range(i1,i1+n):
                    for i4 in range(i2,i2+n):
                        new_array.append(arr[i3][i4])
                nine(n,new_array)
    return t_1,t0,t1

t_1,t0,t1 = 0,0,0
print(*nine(n,g),sep='\n')