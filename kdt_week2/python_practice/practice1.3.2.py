# ☁ 실습 1 ☁

n = int(input('정수를 입력하세요 > '))

if n > 0:
    print(True)
else:
    print(False)

# ☁ 실습 2 ☁

a = int(input('첫 번째 정수를 입력하세요 > '))
b = int(input('두 번째 정수를 입력하세요 > '))
if a == b:
    print(False)
else:
    print(max(a, b))

# ☁ 실습 3 ☁

a = int(input('정수를 입력하세요 > '))

if 1< a < 10:
    print(True)
else:
    print(False)

# ☁ 실습 4 ☁

a = int(input('정수를 입력하세요 > '))

if a > 0:
    if a % 2 == 0:
        print(True)
    else:
        print(False)
else:
    print(False)

# ☁ 실습 5 ☁

a = int(input('정수를 입력하세요 > '))

if 100 >= a >= 60:
    print('합격')
elif 60 > a >= 0:
    print('불합격')
else:
    print('에러')

# ☁ 실습 6 ☁

a = input('문자열을 입력하세요 > ')
i = len(a)
for b in a[i::-1]:
    print(b)

# ☁ 실습 7 ☁

a = int(input('첫 번째 정수를 입력하세요 > '))
b = int(input('두 번째 정수를 입력하세요 > '))

if a == b:
    print(False)
else:
    for c in range(max(a,b) - min(a,b) - 1):
        c += 1
        print(c + min(a,b))

# ☁ 실습 8 ☁

a = int(input('첫 번째 정수를 입력하세요 > '))
b = int(input('두 번째 정수를 입력하세요 > '))

if a == b:
    print(False)
else:
    for c in range(max(a,b) - min(a,b) - 1):
        c += 1
        print(max(a,b) - c,end=' ')

# ☁ 실습 9 ☁

a = int(input('정수를 입력하세요 > '))

if a < 1:
    print(False)
else:
    for b in range(a):
        if b % 2 == 0:
            continue
        print(b)

# ☁ 실습 10 ☁

for n in range(2, 10):
    for m in range(2,10):
        print(f'{n} X {m} = {n*m}')