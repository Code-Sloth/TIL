# 1436 영화감독 숌

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = 666 
i = 1 # 666이 첫 번째 수이기 때문에 1로 설정
num = int(input()) # 500
while 1:
    if '666' in str(n): # 666 o 667 x 668 x ... 1666 o
        if num == i: # i가 500이 되면
            print(n) # 166699
            break # 반복문 중단
        i += 1 # 666이 들어가는 수일 경우에만 +1
    n += 1 # 666 667 668 669 ...