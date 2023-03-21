# ☁ 실습 1 ☁

# 정수 한 개를 입력 받고, 해당 숫자가 0보다 큰 숫자라면 True 아니면 False를 출력하세요

n = int(input('정수를 입력하세요 > '))

if n > 0:
    print(True)
else:
    print(False)

# ☁ 실습 2 ☁

# 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.

# 두 정수가 같으면 False를 출력하세요.

a = int(input('첫 번째 정수를 입력하세요 > '))
b = int(input('두 번째 정수를 입력하세요 > '))
if a == b:
    print(False)
else:
    print(max(a, b))

# ☁ 실습 3 ☁

# 정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.

a = int(input('정수를 입력하세요 > '))

if 1< a < 10:
    print(True)
else:
    print(False)

# ☁ 실습 4 ☁

# 정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True 아니면 False를 출력하세요.

a = int(input('정수를 입력하세요 > '))

if a > 0:
    if a % 2 == 0:
        print(True)
    else:
        print(False)
else:
    print(False)

# ☁ 실습 5 ☁

# 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.

# 값이 100 초과 / 0 미만이면 "에러" 출력
# 값이 60 이상이면 "합격" 출력
# 값이 60 미만이면 "불합격" 출력

a = int(input('정수를 입력하세요 > '))

if 100 >= a >= 60:
    print('합격')
elif 60 > a >= 0:
    print('불합격')
else:
    print('에러')

# ☁ 실습 6 ☁

# 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.

# 힌트 : 문자열 역슬라이싱

a = input('문자열을 입력하세요 > ')
i = len(a)
for b in a[i::-1]:
    print(b)

# ☁ 실습 7 ☁

# 정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.

# 두 값이 같으면 False를 출력하세요

a = int(input('첫 번째 정수를 입력하세요 > '))
b = int(input('두 번째 정수를 입력하세요 > '))

if a == b:
    print(False)
else:
    for c in range(max(a,b) - min(a,b) - 1):
        c += 1
        print(c + min(a,b))

# ☁ 실습 8 ☁

# 정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.

# 두 값이 같으면 False를 출력하세요

a = int(input('첫 번째 정수를 입력하세요 > '))
b = int(input('두 번째 정수를 입력하세요 > '))

if a == b:
    print(False)
else:
    for c in range(max(a,b) - min(a,b) - 1):
        c += 1
        print(max(a,b) - c,end=' ')

# ☁ 실습 9 ☁

# 정수 한 개를 입력 받고, 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요.

# 입력 값이 1보다 작으면 False를 출력하세요.

a = int(input('정수를 입력하세요 > '))

if a < 1:
    print(False)
else:
    for b in range(a):
        if b % 2 == 0:
            continue
        print(b)

# ☁ 실습 10 ☁

# 구구단을 출력하세요.

# 반복

for n in range(2, 10):
    for m in range(2,10):
        print(f'{n} X {m} = {n*m}')