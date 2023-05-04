# 2002 추월
# 34096KB / 64ms

from collections import deque

n = int(input())

in_car = deque()
t = 0
for i in range(2*n):
    if i < n:
        in_car.append(input().rstrip()) # 들어온 차
    else:
        out_car = input().rstrip()      # 나가는 차

        if out_car != in_car[0]:        # 순서가 맞지 않으면
            t += 1                      # 카운트 +1
        in_car.remove(out_car)          # 들어온 차 목록에서 그 차를 제거

print(t)