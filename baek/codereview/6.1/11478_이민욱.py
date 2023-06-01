# 11478 서로 다른 부분 문자열의 개수
# 240716KB / 540ms

import sys
input = sys.stdin.readline

s = input().rstrip()
se = set()
len_s = len(s)

for i in range(len_s):
    for j in range(i, len_s):
        substring = s[i:j+1]
        se.add(substring)

print(len(se))

'''
a
ab
aba
abab
ababc
b
ba
bab
babc
a
ab
abc
b
bc
c

se = {'bab', 'ababc', 'c', 'b', 'ba', 'abab', 'bc', 'aba', 'abc', 'babc', 'a', 'ab'}
'''