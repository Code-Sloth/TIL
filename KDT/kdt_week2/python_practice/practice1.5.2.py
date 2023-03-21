# ☁ 실습 1 ☁

# 문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.

a = input('문자열을 입력하세요 > ')
n = 0

for i in a:
    if 'e' in i:
        n += 1

print(n)

# ☁ 실습 2 ☁

# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.

# 알파벳 모음 : a(A) e(E) i(I) o(O) u(U)

# 단, count() 함수는 사용하지마세요.

a = input('문자열을 입력하세요 > ')
n = 0
c = ['A','a','e','E','i','I','o','O','u','U']

for i in a:
    if i in c:
        n += 1

print(n)

# ☁ 실습 3 ☁

# 입력과 같은 딕셔너리 변수가 있을 때, 해당 인물의 나이를 출력하세요.

dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

dict_variable['나이'] = int(input())

print(f"나이 : {dict_variable['나이']}세")

# ☁ 실습 4 ☁

# 이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고, 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.

name = input('이름을 입력하세요 > ')
num = input('전화번호를 입력하세요 > ')
addr = input('거주지를 입력하세요 > ')

d = {'이름': name,'전화번호' : num,'거주지' : addr}

for key,value in d.items():
    print(key,value,sep=' : ')

# ☁ 실습 5 ☁

# 이름, 전화번호, 이메일, 거주지 정보를 입력받아 출력 예시와 동일한 딕셔너리 구조를 출력하세요.

# Hint : 딕셔너리 안에 딕셔너리를 넣을 수 있습니다.

name = input('이름을 입력하세요 > ')
num = input('전화번호를 입력하세요 > ')
email = input('이메일을 입력하세요 > ')
addr = input('거주지를 입력하세요 > ')

d1 = {'전화번호' : num, '이메일' : email, '거주지' : addr}
d2 = {name : d1}

print(d2)

# ☁ 실습 6 ☁

# 문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.

a = input()
d = {}
n = 1

for j in a:
    if j in d:
        n += 1
        d[j]=n
    else:
        d[j]=1


for key,value in d.items():
    print(key,value,sep=' : ')