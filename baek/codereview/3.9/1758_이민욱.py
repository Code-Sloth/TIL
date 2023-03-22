# 1758 알바생 강호
# 35892KB / 92ms

n = int(input())
q = sorted([int(input()) for _ in range(n)],reverse=True) # 큰 수일수록 덜깎이게
t = 0

for i in range(n):
    sub = q[i] - i # 인덱스만큼 빼기
    if sub > 0: # 0 이상일 때
        t += sub

print(t)