import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

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