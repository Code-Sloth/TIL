# 10448 유레카 이론

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

li = [i*(i+1)//2 for i in range(1,46)]

def ureka(li, n):
    for i in li:
        for j in li:
            for k in li:
                if i + j + k == n:
                    return 1
    return 0
            
for _ in range(int(input())):
    print(ureka(li,int(input())))