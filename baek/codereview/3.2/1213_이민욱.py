# 1213 팰린드롬 만들기
# 31256KB / 44ms

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

q = sorted(list(input().rstrip()),reverse=True)
s,last = '',''
t = 0

for i in sorted(list(set(q)),reverse=True)[::-1]:
    cnt = q.count(i) # q에서 i문자의 개수를 cnt에 저장
    if cnt % 2 == 1:
        t += 1 # 문자의 개수가 홀수인 개수
        last = i # 문자의 개수가 홀수인 문자를 저장
        s += i * (cnt//2) # AAA 면 A만 담음
        for _ in range(cnt): q.pop() # 다음 문자열을 탐색해야하니 현재 문자열들을 모두 삭제
    elif cnt % 2 == 0:
        s += i * (cnt//2) # AAAA면 AA만 담음
        for _ in range(cnt): q.pop()
    if t > 1: print("I'm Sorry Hansoo"); sys.exit()

s += last # 문자의 개수가 홀수인 문자를 center로 배치

if not t: # 문자의 개수가 모두 짝수면
    s += s[::-1] # 전체를 반대로 복사하고 담음
else: # 문자의 개수가 홀수인 문자가 있으면
    s += s[-2::-1] # center를 제외하고 반대로 복사하고 담음
print(s)
