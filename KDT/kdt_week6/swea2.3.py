# 5431 민석이의 과제 체크하기

for t in range(1, int(input())+1):
    n, k = map(int,input().split())
    li = list(map(int,input().split()))
    li2 = []
    for i in range(1,n+1):
        if i not in li:
            li2.append(i)
    print(f'#{t}',*li2)

# 2001 파리 퇴치

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

for t in range(1,int(input())+1):
    n, m = map(int,input().split())
    li = [list(map(int,input().split())) for _ in range(n)]
    
    cnt_li = []
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for ii in range(m):
                for jj in range(m):
                    cnt += li[i+ii][j+jj]
            cnt_li.append(cnt)

    print(f'#{t}', max(cnt_li))

# 1983 조교의 성적 매기기

credit = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for t in range(1,int(input())+1):
    n, k = map(int,input().split())
    po = [0] * n
    for i in range(n):
        li = list(map(int,input().split()))
        po[i] = li[0] * 0.35 + li[1] * 0.45 + li[2] * 0.20
    me = po[k-1]
    po.sort(reverse=True)
    me_grade = po.index(me)
    print(f'#{t}',credit[me_grade//(n//10)])

# 1979 어디에 단어가 들어갈 수 있을까

for t in range(1,int(input())+1):
    n, k = map(int,input().split())
    li = [list(input().split()) for _ in range(n)]
    li_T = [list(_) for _ in zip(*li)]

    total = 0
    for i in range(n):
        li[i] = ''.join(li[i])
        li_T[i] = ''.join(li_T[i])
        li[i] = li[i].split('0')
        li_T[i] = li_T[i].split('0')
        total += (li[i].count('1'*k) + li_T[i].count('1'*k))
        
    print(f'#{t}',total)

# 1225 암호생성기

from collections import deque

for _ in range(10):
    t = int(input())
    q = deque(list(map(int,input().split())))
    i = 1

    while 1:
        qq = q.popleft() - i
        if qq > 0:
            q.append(qq)
            if i < 5:
                i += 1
            else: i = 1
        else:
            q.append(0)
            break
    print(f'#{t}',*q)

# 1218 괄호 짝짓기

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

paren = ['()','[]','{}','<>']

for t in range(1,11):
    ls = int(input())
    s = input().strip()

    while 1:
        for i in paren:
            s = s.replace(i,'')
        if '()' not in s and '[]' not in s and '{}' not in s and '<>' not in s:break
    
    print(f'#{t}', 0) if s else print(f'#{t}', 1)