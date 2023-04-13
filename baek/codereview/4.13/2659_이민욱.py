# 2659 십자카드 문제
# 31256KB / 56ms

g = input().split() # 문자열로 받음

def func(n): # 시계수로 만드는 함수
    min = int(n) # 정수형으로
    for i in range(1,4):
        a = int(''.join(n[i:] + n[:i])) # 회전
        if min > a:
            min = a
    return min # 최솟값 리턴

t = 1
for i in range(1111, func(''.join(g))): # 1111부터 받은 입력의 시계수까지
    if '0' not in list(str(i)) and i == func(str(i)): # 0이 없고, i가 십자수일 때
        t += 1 # 카운트 +1
print(t)