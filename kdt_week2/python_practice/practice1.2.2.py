# ☁ 실습 1 ☁


''' 출력 예시
정수형 숫자를 입력해주세요 > 10 # 사용자 입력 
20
'''
num1 = input('숫자를 입력해주세요 > ')
print(int(num1) + 10)

# ☁ 실습 2 ☁

''' 출력 예시
좋아하는 음식을 입력해주세요 > 피자 # 사용자 입력 
좋아하는 음식 : 피자
'''
menu = input('좋아하는 음식을 입력해주세요 > ')
print('좋아하는 음식 :', menu)

# ☁ 실습 3 ☁

''' 출력 예시
이름을 입력해주세요 > 정우영 # 사용자 입력 
태어난 년도를 입력해주세요 > 2004 # 사용자 입력
저의 이름은 정우영이고, 올해 나이는 20세 입니다.
'''
name1 = input('이름을 입력해주세요 > ')
year1 = int(input('태어난 년도를 입력해주세요 > '))
year2 = 2024 - year1
print('저의 이름은 {0}이고, 올해 나이는 {1}세 입니다.'.format(name1, year2))

# ☁ 실습 4 ☁

''' 출력 예시
첫 번째 문장을 입력해주세요 > hello # 사용자 입력
두 번째 문장을 입력해주세요 > world # 사용자 입력
helloworld
'''
sentence1 = input('첫 번째 문장을 입력해주세요 > ')
sentence2 = input('두 번째 문장을 입력해주세요 > ')
print(sentence1 + sentence2)

# ☁ 실습 5 ☁

''' 출력 예시
정수형 숫자를 입력해주세요 > 10 # 사용자 입력
-10
'''
num2 = int(input('숫자를 입력해주세요 > '))
num2 = - num2
print(num2)

# ☁ 실습 6 ☁

''' 출력 예시
첫 번째 정수형 숫자를 입력해주세요 > 10 # 사용자 입력
두 번째 정수형 숫자를 입력해주세요 > 3  # 사용자 입력
더하기 연산 : 13
뺴기 연산 : 7
곱하기 연산 : 30
몫 연산 : 3
나머지 연산 : 1
'''
num3 = int(input('첫 번째 숫자를 입력해주세요 > '))
num4 = int(input('두 번째 숫자를 입력해주세요 > '))
print('더하기 연산 : {0}'.format(num3 + num4))
print('빼기 연산 : {0}'.format(num3 - num4))
print('곱하기 연산 : {0}'.format(num3 * num4))
print('몫 연산 : {0}'.format(num3 // num4))
print('나머지 연산 : {0}'.format(num3 % num4))

# ☁ 실습 7 ☁

''' 출력 예시
첫 번째 정수형 숫자를 입력해주세요 > 1 # 사용자 입력
두 번째 정수형 숫자를 입력해주세요 > 2 # 사용자 입력
세 번째 정수형 숫자를 입력해주세요 > 3 # 사용자 입력
2
'''
num5 = int(input('첫 번째 숫자를 입력해주세요 > '))
num6 = int(input('두 번째 숫자를 입력해주세요 > '))
num7 = int(input('세 번째 숫자를 입력해주세요 > '))
num8 = (num5 + num6 + num7) // 3
print(num8)

# ☁ 실습 8 ☁

''' 출력 예시
첫 번째 정수형 숫자를 입력해주세요 > 2   # 사용자 입력
두 번째 정수형 숫자를 입력해주세요 > 54  # 사용자 입력
세 번째 정수형 숫자를 입력해주세요 > 1   # 사용자 입력
네 번째 정수형 숫자를 입력해주세요 > 6   # 사용자 입력
다섯 번째 정수형 숫자를 입력해주세요 > 3  # 사용자 입력
[2, 54, 1, 6, 3]
'''
num9 = int(input('첫 번째 숫자를 입력해주세요 > '))
num10 = int(input('두 번째 숫자를 입력해주세요 > '))
num11 = int(input('세 번째 숫자를 입력해주세요 > '))
num12 = int(input('네 번째 숫자를 입력해주세요 > '))
num13 = int(input('다섯 번째 숫자를 입력해주세요 > '))
nums = [num9, num10, num11, num12, num13]
list_nums = list(nums)
print(list_nums)

# ☁ 실습 9 ☁

''' 출력 예시
문자열을 입력해주세요 > hello # 사용자 입력
정수형 숫자를 입력해주세요 > 3 # 사용자 입력
hellohellohello
'''
str1 = input('문자열을 입력해주세요 > ')
num_a = int(input('숫자를 입력해주세요 > '))
print(str1 * num_a)

# ☁ 실습 10 ☁

''' 출력 예시
첫 번째 정수형 숫자를 입력해주세요 > 1  # 사용자 입력
1
두 번째 정수형 숫자를 입력해주세요 > 2  # 사용자 입력
3
세 번째 정수형 숫자를 입력해주세요 > 3  # 사용자 입력
6
네 번째 정수형 숫자를 입력해주세요 > 4  # 사용자 입력
10
다섯 번째 정수형 숫자를 입력해주세요 > 5 # 사용자 입력
15
'''

''' solution 1
num14 = int(input('첫 번째 숫자를 입력해주세요 > '))
print(num14)
num15 = int(input('두 번째 숫자를 입력해주세요 > '))
print(num14 + num15)
num16 = int(input('세 번째 숫자를 입력해주세요 > '))
print(num14 + num15 + num16)
num17 = int(input('네 번째 숫자를 입력해주세요 > '))
print(num14 + num15 + num16 + num17)
num18 = int(input('다섯 번째 숫자를 입력해주세요 > '))
print(num14 + num15 + num16 + num17 + num18)
'''

# solution 2

number1 = int(input("첫 번째 숫자를 입력해주세요 > "))
num = 0
num += number1
print(num)
number2 = int(input("두 번째 숫자를 입력해주세요 > "))
num += number2
print(num)
number3 = int(input("세 번째 숫자를 입력해주세요 > "))
num += number3
print(num)
number4 = int(input("네 번째 숫자를 입력해주세요 > "))
num += number4
print(num)
number5 = int(input("다섯 번째 숫자를 입력해주세요 > "))
num += number5
print(num)