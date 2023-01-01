# ☁ if ☁

# weather = "비"
# if 조건:
#      실행 명령문

weather = "비" # "맑아요" = 마스크를 챙기세요 / 그 외 = 준비물 필요 없어요.
if weather == "비":
     print("우산을 챙기세요")
elif weather == "미세먼지":
     print("마스크를 챙기세요")
else:
     print("준비물 필요 없어요.")

'''
 weather = input("오늘 날씨는 어때요? ") # 터미널 창에서 대답하면 그에 맞게 출력
 if weather == "비" or weather == "눈":
      print("우산을 챙기세요")
 elif weather == "미세먼지":
      print("마스크를 챙기세요")
 else:
      print("준비물 필요 없어요.")

 temp = int(input("기온은 어때요? "))
 if 30 <= temp:
      print("너무 더워요. 나가지 마세요")
 elif 10 <= temp and temp < 30:
      print("괜찮은 날씨예요")
 elif 0 <= temp < 10:
      print("외투를 챙기세요")
 else:
      print("너무 추워요. 나가지 마세요")
'''

# ☁ for ☁

print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [0,1,2,3,4]:
     print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6): # 1,2,3,4,5
     print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
     print("{0}, 커피가 준비되었습니다.".format(customer))

# ☁ while ☁

customer = "토르"
index = 5
while index >= 1: # while (조건):
     print("{0}, 커피가 준비 되었습니다, {1}번 남았어요.".format(customer, index))
     index -= 1
     if index == 0:
          print("커피는 폐기처분되었습니다.")

'''
customer2 = "아이언맨"
i = 1
while True:
     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer2, i))
     i += 1
''' # 무한 반복

'''
cust = "토르"
person = "Unknown"

while person != cust:
     print("{0}, 커피가 준비 되었습니다.".format(cust))
     person = input("이름이 어떻게 되셔요? ")
'''

# ☁ continue 와 break ☁

absent = [2, 5] # 결석
no_book = [7] # 책을 안들고 옴

for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
     if student in absent:
          continue
     elif student in no_book:
          print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
          break
     print("{0}, 책을 읽어봐".format(student))

# ☁ 한줄 for ☁

# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


# ================================================================================
# Quiz 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다. # 난수 = 랜덤
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [0] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분
# ================================================================================


# my solution

''' # 두개 다 오류남...
from random import *

min = range(5,51)
min = list(min)
shuffle(min)
minute = sample(min, 1)
i1 = range(5,16)
i2 = range(16,51)

for guest in range(1,51):
     if minute in i1:
          print("[0] {0}번째 손님 (소요시간 : {1}분)".format(guest, minute))
     elif minute in i2:
          print("[ ] {0}번째 손님 (소요시간 : {1}분".format(guest, minute))


min = range(5,51)
minute = sample(min,1)
i = 1
board = range(5,16)
not_board = range(16,51)

while i <= 50:
    minute = sample(min,1)
    i += 1
    if minute in board:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, minute))
    elif minute in not_board:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, minute))

        # 이건 되는데 (밑에 코드)

min = range(5,51)

for guest in range(1,51):
     minute = randrange(5,51)
     if 5 <= minute <= 15:
          print("[O] {0}번째 손님 (소요시간 : {1}분)".format(guest, minute))
     else:
          print("[ ] {0}번째 손님 (소요시간 : {1}분".format(guest, minute))

          # 이건 왜 안되지? (밑에 코드)

min = range(5,51)

for guest in range(1,51):
     minute = sample(min, 1)
     if 5 <= minute <= 15:
          print("[O] {0}번째 손님 (소요시간 : {1}분)".format(guest, minute))
     else:
          print("[ ] {0}번째 손님 (소요시간 : {1}분".format(guest, minute))
          '''

from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50 이라는 승객 수
     time = randrange(5, 51) # 5분 ~ 50분 소요 시간
     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
          print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
          cnt += 1
     else: # 매칭 실패한 경우
          print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
          
print("총 탑승 승객 : {0}".format(cnt))

# ☁ 함수 ☁

def open_account():
     print("새로운 계좌가 생성되었습니다.")

open_account()

# ☁ 전달값과 반환값 ☁

def deposit(balance, money): # 입금
     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
     return balance + money

def withdraw(balance, money): # 출금
     if balance >= money: # 잔액이 출금보다 많으면
          print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
          return balance - money
     else:
          print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
          return balance

def withdraw_night(balance, money): # 저녁에 출금
     commission = 100 # 수수료 100원
     return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))


# ☁ 기본값 ☁

'''
def profile(name, age, main_lang):
     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
             .format(name, age, main_lang)) # \ 줄바꿈
     
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")
'''

# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age=17, main_lang="파이썬"):
     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
             .format(name, age, main_lang))
     
profile("유재석")
profile("김태호")

# ☁ 키워드 값 ☁

def profile(name, age, main_lang):
     print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

# ☁ 가변인자 ☁

'''
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end" " 줄바꿈을 하지않고 이어서 출력
     print(lang1, lang2, lang3, lang4, lang5)
'''

def profile(name, age, *language): # * 가변인자
     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end" " 줄바꿈을 하지않고 이어서 출력
     for lang in language:
          print(lang, end=" ")
          print()

profile("유재석", 20, "python", "java", "c", "c++", "c#", "javascript")
profile("김태호", 25, "kotlin", "swift", "", "", "")

# ☁ 지역변수와 전역변수☁

'''
gun = 10

def checkpoint(soldiers): # 경계근무
     gun = 20 # 지역 변수
     gun = gun - soldiers
     print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계근무 나감
print("남은 총 : {0}".format(gun))
''' # 전체 총 10 / 함수 내 남은 총 18 / 남은 총 10가 됨

'''
gun = 10

def checkpoint(soldiers): # 경계근무
     global gun # 전역 공간에 있는 gun 사용
     gun = gun - soldiers
     print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계근무 나감
print("남은 총 : {0}".format(gun))
'''
# 일반적으로 전역변수를 많이 쓰면 코드 관리가 어려워서 권장되지 않음
# 가급적 함수의 전달값으로 던져서 계산하고 반환값을 받아서 사용하는 방법 아래에 나옴

gun = 10

def checkpoint(soldiers): # 경계근무
     global gun # 전역 공간에 있는 gun 사용
     gun = gun - soldiers
     print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
     gun = gun - soldiers
     print("[함수 내] 남은 총 : {0}".format(gun))
     return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

# ===============================================
# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#  남자 : 키(m) x 키(m) x 22
#  여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#             * 함수명 : std_weight
#             * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.
# ===============================================


# my solution

'''
def std_weight(height, gender):
     if gender == "남자":
          weight = height * height * 22 / 10000
          print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
     elif gender == "여자":
          weight = height * height * 211 / 10000
          print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

std_weight(int(input("키를 입력해 주세요. ")), gender = input("성별을 입력해 주세요. "))
'''
# solution

def std_weight(height, gender): # 키 m 단위 (실수), 성별 "남자" / "여자"
     if gender == "남자":
          return height * height * 22
     else:
          return height * height * 21
     
height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))