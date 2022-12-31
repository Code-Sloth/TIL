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

print(name + "는 어른일까요? " + str(is_adult))

