# 25632 소수 부르기 게임
# 31256KB / 44ms

# https://this-programmer.tistory.com/409

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 예제 입력 4 기준
a,b = map(int,input().split()) # 11 17
c,d = map(int,input().split()) # 13 19

def sosu(n): # 에라토스테네스의 체 (구간 내 모든 소수 구하기)
    li = [1] * (n+1) # 1 : 소수 / 0 : 소수x
    for i in range(2,int(n**0.5)+1): # 제곱근까지만 반복
        if li[i]: 
            for j in range(i*2,n+1,i): # 배수들을 모두 소수x로 만듦
                li[j] = 0
    return [num for num in range(2,n+1) if li[num]] # 소수인 인덱스들만 

g = sosu(max(a,b,c,d)) # 최댓값까지 소수를 구해서 담음
# [2, 3, 5, 7, 11, 13, 17, 19]

yt = yj = mid = 0
for i in g:
    if a <= i <= b: yt += 1 # [11, 13, 17]
    if c <= i <= d: yj += 1 # [13, 17, 19]
    if c <= i <= b or a <= i <= d: mid += 1 # [13, 17]

if yt > yj: print('yt')
elif yt < yj: print('yj')
else:
    if mid % 2 == 1: print('yt')
    else: print('yj')

# mid 짝수 / 예제 입력 4

#               용태       용진      중간
#            [11,13,17] [13,17,19] [13,17]

#1 용태17    [11,13]    [13,19]    [13]
#2 용진13     [11]       [19]     
#3 용태11                [19]

#                       용진 승



# mid 홀수 / 예제 입력 3

#               용태       용진      중간
#              [5,7]      [7,11]    [7]

#1 용태7        [5]        [11]   
#2 용진11       [5]    

#              용태 승