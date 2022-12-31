print("hello world")
print(5)
print(3.14)
print(10000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print("ㅋ"*9)

# 참 / 거짓
print(5 > 10)
print(5 < 10)
print(not True)
print(not False)
print(not (5 > 10))

# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3



print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 좋아해요") 
print("연탄이는 어른일까요? True")

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, " + hobby + " 을 아주 좋아해요 ")
# 정수형은 str로 감싸줘야 한다.

print(name + "는 ",age,"살이며, ",hobby,"을 아주 좋아해요 ")
# +는 ,로 바꿔줘도 된다. 그럼 정수형 str을 붙일 필요 없다.
# ,를 넣으면 자동 띄어쓰기가 된다.

print(name + "는 어른일까요? " + str(is_adult))

# '''여러문장을 주석처리'''
# 여러 줄을 드래그 한 다음 Ctrl + / 입력하면 한번에 주석처리

# =================================================
# Quiz 변수를 이용하여 다음 문장을 출력하시오

# 변수명 : Station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장 : XX행 열차가 들어오고 있습니다.
# =================================================

Station = "사당"
print(Station + "행 열차가 들어오고 있습니다.")
Station = "신도림"
print(Station + "행 열차가 들어오고 있습니다.")
Station = "인천공항"
print(Station + "행 열차가 들어오고 있습니다.")

# ☁ 연산자

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 1
print(5//3) # 1
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True
# == 같다 != 같지 않다
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True
# or = | 둘 중 하나만 맞으면 True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

# ☁ 간단한 수식 ☁

num = 2 + 3 * 4
print(num) # 14
num = num + 2
print(num) # 16
num += 2
print(num) # 18
num *= 2 
print(num) # 36
num /= 2
print(num) # 18
num -= 2
print(num) # 16
num %= 5
print(num) # 1

# ☁ 숫자 처리 함수 ☁

print(abs(-5)) # 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 반올림 3
print(round(4.99)) # 5

from math import *
# math안에 있는 모든 라이브러리를 이용하겠다

print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

# ☁ 랜덤 함수 ☁

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 정수 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 정수 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 정수 임의의 값 생성 / lotto
print(randint(1, 45)) # 1 ~ 45 이하의 정수 임의의 값 생성


# ==========================================================================
# Quiz 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
# ==========================================================================


date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")

# ☁ 문자열 ☁ (46.57)

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)   
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""

# ☁ 슬라이싱 ☁ (46.57)

jumin = "990120-1234567"
# 첫 9는 0번째 숫자

print("성별 : " + jumin[7]) # 1
print("연 : " + jumin[0:2]) # 0 ~ 2번째 직전까지 / 99
print("월 : " + jumin[2:4]) # 01
print("일 : " + jumin[4:6]) # 20
print("생년월일 :" + jumin[:6]) # 처음부터 6번째 직전까지 / 990120
print("뒤 7자리" + jumin[7:]) # 7번째부터 끝까지 / 1234567
print("뒤 7자리 (뒤에서부터)" + jumin[-7:]) # 뒤에서 7번째부터 끝까지 / 1234567

# ☁ 문자열 처리 함수 ☁ (46.57)

python = "Python is Amazing"
print(python.lower()) # 소문자로만 출력
print(python.upper()) # 대문자로만 출력
print(python[0].isupper()) # 첫번째가 대문자야? / True
print(len(python)) # 파이썬 문자열의 길이 / 17
print(python.replace("Python", "Java")) # Python의 문자열을 Java로 바꿔줌

index = python.index("n") # n이 몇번째 위치?
print(index)
index = python.index("n", index + 1) # 두번째 n은 몇번째 위치?
print(index)

print(python.find("n")) # 똑같이 n이 몇번째 위치?
print(python.find("Java")) # 원하는 값이 없을 경우 -1
# print(python.index("Java")) # 오류가 뜸
print("hi") # find는 보이지만 index는 안보임

print(python.count("n")) # n이 총 몇번 등장?

# ☁ 문자열 포맷 ☁ (46.57)

