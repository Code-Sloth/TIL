# 1406 에디터
# 41856KB / 328ms

from collections import deque

q = deque(list(input().rstrip()))
m = int(input())
c = len(q) # 커서 위치
rota = 0 # 회전 횟수

for _ in range(m):
    o = input().split()
    if o[0] == 'L' and c > 0: # L이고 젤 왼쪽이 아니면
        c -= 1
        q.rotate(1)
        rota -= 1
    elif o[0] == 'D' and c < len(q): # D이고 젤 오른쪽이 아니면
        c += 1
        q.rotate(-1)
        rota += 1
    elif o[0] == 'B' and c > 0: # B이고 젤 왼쪽이 아니면
        c -= 1
        q.pop()
    elif o[0] == 'P': # P일 때
        c += 1
        q.append(o[1])

# 회전 횟수만큼 반대로 회전해서 처음 상태로
if rota > 0:
    for _ in range(rota):
        q.rotate(1) 
if rota < 0:
    for _ in range(-rota):
        q.rotate(-1)

print(''.join(q))