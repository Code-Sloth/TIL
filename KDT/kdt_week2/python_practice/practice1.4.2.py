# ☁ 실습 1 ☁

# 정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.

# 단, abs() 함수는 사용하지 마세요.

a = int(input('정수를 입력하세요 > '))

if a < 0:
    a = (-a)

print(a)

# ☁ 실습 2 ☁

# 정수만 저장한 리스트가 주어집니다.

# 리스트 요소의 개수를 출력하세요.

# 단, len() 함수는 사용하지 마세요

# 입력 1

number_list = [1, 2, 3, 4, 5]
n = 0

for i in number_list:
    n += 1

print(n)

# 입력 2

number_list = []
n = 0

for i in number_list:
    n += 1

print(n)

# ☁ 실습 3 ☁

# 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수들의 합을 출력하세요.

# 단, sum() 함수는 사용하지 마세요.

# 입력 1

number_list = [1, 2, 3, 4, 5]
n = 0

for i in number_list:
    n += i

print(n)

# 입력 2

number_list = [-1, -2, -3, -4, -5]
n = 0

for i in number_list:
    n += i

print(n)

# ☁ 실습 4 ☁

# 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수들의 평균을 출력하세요.

# 단, len() / sum() 함수는 사용하지 마세요.

# 입력 1

number_list = [2, 4, 6]
n = 0
m = 0

for i in number_list:
    n += i
    m += 1

print(n/m)

# 입력 2

number_list = [2, 3, 5, 7]
n = 0
m = 0

for i in number_list:
    n += i
    m += 1

print(n/m)

# ☁ 실습 5 ☁

# 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수들의 곱을 출력하세요.

# 입력 1

number_list = [1, 2, 3, 4, 5]
n = 1

for i in number_list:
    n *= i

print(n)

# 입력 2

number_list = [-1, -2, 3]
n = 1

for i in number_list:
    n *= i

print(n)

# ☁ 실습 6 ☁

# 양의 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수 중 가장 큰 값을 출력하세요.

# 단, max() 함수는 사용하지 마세요.

# 입력 1

number_list = [1, 2, 3, 4, 5]
n = number_list[0]
max_num = n

for i in number_list:
    if max_num <= i:
        max_num = i

print(max_num)

# 입력 2

number_list = [1, 1, 1]
n = number_list[0]
max_num = n

for i in number_list:
    if max_num < i:
        max_num = i

print(max_num)

# ☁ 실습 7 ☁

# 양의 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수 중 가장 작은 값을 출력하세요.

# 단, min() 함수는 사용하지 마세요.

# 입력 1

number_list = [1, 2, 3, 4, 5]
n = number_list[0]
min_num = n

for i in number_list:
    if min_num > i:
        min_num = i

print(min_num)

# 입력 2

number_list = [5, 5, 5, 2]
n = number_list[0]
min_num = n

for i in number_list:
    if min_num > i:
        min_num = i

print(min_num)
