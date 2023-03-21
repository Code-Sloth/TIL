# 2576 홀수

li = []
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        li.append(n)
if li == []:
    print(-1)
else:
    print(sum(li),min(li),sep = '\n')

# 10822 더하기

print(sum(list(map(int,input().split(',')))))

# 2754 학점계산

po = list(input())

di = {'A':4, 'B':3, 'C':2, 'D':1, '+':+0.3, '0':+0.0, '-':-0.3}
if po == ['F']: print(0.0)
else:print(di[po[0]]+di[po[1]])

# 5622 다이얼

import string
al = string.ascii_uppercase
nums = '22233344455566677778889999'
tr = str.maketrans(al,nums)
s = input()
t = len(s)
s = s.translate(tr)
for i in s:
    t += int(i)
print(t)

# 2577 숫자의 개수

n = 1
for _ in range(3):
    n *= int(input())

for i in range(10):
    print(str(n).count(str(i)))

# 7785 회사에 있는 사람

di = {}
for _ in range(int(input())):
    a,b = input().split()
    di[a] = b
di2 = di.copy()

for i in di2:
    if di2[i] == 'leave':
        del di[i]

print(*sorted(di.keys(),reverse=True),sep='\n')