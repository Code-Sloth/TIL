# ☁ 문자열 포맷 ☁

# print("a" + "b")
# print("a", "b")

# 방법 1

print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" % "A")
# %s는 다 된다.
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." %("파랑", "빨강"))

# 방법 2

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파랑", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파랑", "빨강"))

# 방법 3

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨강"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨강", age = 20))

# 방법 4 (V3.6 이상 가능)

age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# ☁ 탈출 문자 ☁

print("백문이 불여일견 \n백견이 불여일타") # \n = 줄바꿈

print("저는 '아무개'입니다.")
print('저는 "아무개"입니다.')
print("저는 \'아무개\'입니다.")
print('저는 \"아무개\"입니다.') # \" \' : 문장 내에서 따옴표
print("c:\\Users\\pc1\\Desktop\\Code-Sloth\\TIL") # \\ : \ 출력
print("Red Apple\rPine") # \r : 커서를 맨 앞으로 이동 문자 길이 만큼 앞에걸 덮음
print("Redd\bApple") # \b : 한글자 삭제
print("Red\tApple") # /t : 탭

# ============================================================================
# Quiz 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# ex) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점 (.)포함 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                  (nav)              (5)             (1)        (!)
# ex) 생성된 비밀번호 : nav51!
# ============================================================================

# my solution
url = "http://kakao.com"
url = url[7:]
url = url[:-4] # .의 위치로 해야해서 잘못됐다.

print(url[:3] + str(len(url)) + str(url.count("e")) + "!")


# solution
url2 = "http://naver.com"
my_str = url2.replace("http://", "") # 규칙 1
# inde = url2.index("/")
# my_str = url2[inde + 2:] 도 되긴 한데 복잡함..

# print(my_str)
my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0 ~ 5 직전까지
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url2, password))

# ☁ 리스트 ☁

# 지하철 칸별로 10명, 20명, 30명

# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # 하하 추가
print(subway)

# 정형돈을 유재석 / 조세호 사이에 태워본다.
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num = [5,2,4,3,1]
num.sort()
print(num)

# 순서 뒤집기
num.reverse()
print(num)

# 모두 지우기
num.clear()
print(num)

# 다양한 자료형과 함께 사용
num = [5,2,4,3,1]
mix = ["조세호", 20, True]
print(mix)

# 리스트 확장
num.extend(mix)
print(num)

# ☁ 사전 ☁

cabinet = {3:"유재석", 100:"김태호"} # 열쇠 3 유재석이 쓰고 있다.
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])는 오류
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"a-3":"유재석", "b-100":"김태호"}
print(cabinet["a-3"])
print(cabinet["b-100"])

# 새 손님
print(cabinet)
cabinet["a-3"] = "김종국"
cabinet["c-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["a-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

# ☁ 튜플 ☁

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 오류 - 튜플은 add불가

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# ☁ 세트 (집합) ☁

# 중복, 순서 X

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union((python)))

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹었음
java.remove("김태호")
print(java)

# ☁ 자료구조의 변경 ☁

menu = {"커피", "우유", "주스"}
print(menu, type(menu)) 

menu = list(menu)
print(menu, type(menu)) # type이 list로 바뀜 / {}중괄호 >> []대괄호

menu = tuple(menu)
print(menu, type(menu)) # list가 tuple로 바뀜 / []대괄호 >> ()소괄호

menu = set(menu)
print(menu, type(menu)) # tuple이 set로 바뀜 / ()소괄호 >> {}중괄호


# =====================================================================
# Quiz 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 참석자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건 2 : 댓글 내용과 상관없이 무작위로 추첨하되 활용 불가
# 조건 3 : random 모듈의 shuffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))
# =====================================================================

from random import *
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(lst)
print("-- 당첨자 발표 --\n치킨 당첨자 : " + str(sample(lst, 1)) + "\n커피 당첨자 : " + str(lst[:3]) + "\n-- 축하합니다 --")

users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users))
users = list(users) # range를 list로 변환
# print(type(users))
print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")