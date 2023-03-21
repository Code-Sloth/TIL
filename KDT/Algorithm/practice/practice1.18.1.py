# 10988 팰린드롬인지 확인하기

s = input()
if s == s[::-1]:
    print(1)
else:
    print(0)

# 2675 문자열 반복

for _ in range(int(input())):
    n,s = input().split()
    for i in s:
        print(i*int(n),end='')
    print()

# 2789 유학 금지

s = input()
camb = 'CAMBRIDGE'
for i in s:
    if i in camb:
        s = s.replace(i,'')
print(s)

# 2941 크로아티아 알파벳

li = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = input()
for i in li:
    s = s.replace(i,'*')
print(len(s))

# 10809 알파벳 찾기

import string

low = string.ascii_lowercase
s = input()

for i in low:
    print(s.find(i),end=' ')

# 17249 태보태보 총난타

s = input()
t = 0

for i in s:
    if i == '@':
        t += 1
    elif i == '^':
        break
print(t,s.count('@')-t)