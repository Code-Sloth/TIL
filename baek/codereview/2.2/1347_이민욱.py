# 1347 미로 만들기

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 예제 입력 2 기준
n = int(input()) # 6
ord = list(input().rstrip()) # LFFRFF
li = [['#'] * 101 for _ in range(101)] # 최대 50정도 이동 => 101 x 101 이차원 리스트 생성
li_i = [50] # i의 경로
li_j = [50] # j의 경로
i,j = 50,50 # index
li[50][50] = '.' # 기준점
t = 4 # 방향

for order in ord: # 'L' 'F' 'F' 'R' 'F' 'F'
    if order == 'R':
        t += 1
    elif order == 'L':
        t -= 1
    elif order == 'F':
        if t % 4 == 0: 
            i += 1
            li[i][j] = '.'
            li_i.append(i)
        elif t % 4 == 1: 
            j -= 1
            li[i][j] = '.'
            li_j.append(j)
        elif t % 4 == 2: 
            i -= 1
            li[i][j] = '.'
            li_i.append(i)
        else: 
            j += 1
            li[i][j] = '.'
            li_j.append(j)
# 50 50
# t = 3 
# 50 51
# 50 52
# t = 4
# 51 52
# 52 52

# li_i = [50,51,52]
# li_j = [50,51,52]
for ii in range(min(li_i),max(li_i)+1): # 50~52
    for jj in range(min(li_j),max(li_j)+1): # 50~52
        print(li[ii][jj],end='')
    print()