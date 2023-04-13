# 2659 십자카드 문제
# 31256KB / 56ms

g = input().split()

def func(n):
    min = int(n)
    for i in range(1,4):
        a = int(''.join(n[i:] + n[:i]))
        if min > a:
            min = a
    return min

t = 1
for i in range(1111, func(''.join(g))):
    if '0' not in list(str(i)) and i == func(str(i)):
        t += 1
print(t)