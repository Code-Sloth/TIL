# 13335 트럭
# 34140KB / 92ms

from collections import deque

n, l, w = map(int,input().split())
li = deque(list(map(int,input().split())))
q = deque([0 for _ in range(l)])

t = 0
while q:
    q.popleft()
    t += 1
    if li:
        if sum(q) + li[0] <= w:
            q.append(li.popleft())
        else:
            q.append(0)

print(t)