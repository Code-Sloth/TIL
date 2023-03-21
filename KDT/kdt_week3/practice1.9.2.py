# ☁ 실습 1 ☁

# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.

# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.

# 단, index() / find() 메서드는 사용하지마세요.

s = input('문자열을 입력하세요 > ')
t = -1

for i in s:
    t += 1
    if i == 'e':
        print(t)
        break
if 'e' not in s:
    print(-1)



# ☁ 실습 2 ☁

# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.

# 단, count() 메서드는 사용하지마세요.

s = list(input('문자열을 입력하세요 > ').split())
d = dict.fromkeys(s)

for i in d:
    d[i] = 0
for j in s:
    d[j] += 1
for k,v in d.items():
    print(k,v)

# ☁ 실습 3 ☁

# 문자열을 입력받고, e 를 제거한 결과를 출력하세요.

# 단, replace() 메서드는 사용하지 마세요.

s = list(input('문자열을 입력하세요 > '))

for i in s:
    if 'e' in s:
        del s[s.index('e')]

print(''.join(s))

# ☁ 실습 4 ☁

# 문자열과 알파벳을 공백으로 구분해서 입력받고,문자열에서 입력한 알파벳의 개수를 출력하세요.

# 단, count() 메서드는 사용하지마세요.

s = list(input('문자열을 입력하세요 > ').split())
t = 0

for i in s[0]:
    if s[1] in i:
        t += 1
        
print(t)

# ☁ 실습 5 ☁

# 양의 정수 3개를 입력받고, 3개의 양수를 - 로 연결해서 출력하세요.

# 단, join() 메서드는 사용하지마세요.

s = list(input('문자열을 입력하세요 > ').split())
s2 = ''

for i in range(len(s)-1):
    s2 = s2 + s[i] + '-'
    
print(s2 + s.pop())

# ☁ 실습 6 ☁

# 양의 정수를 입력받고, 자리수의 합을 출력하세요.

# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.

# 단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.

num = int(input())
li = []
sum = 0

if num < 0:
    print(-1)
else:
    for i in range(20,0,-1):
        num = num % (10**i)
        if num not in li:
            li.append(num)

for j in range(len(li)-1):
    li[j] -= li[j+1]

for k in range(len(li)-1,-1,-1):
    n = li[len(li)-1-k]//(10**k)
    sum += n

print(sum)

# solution 2

data6 = int(input('양의 정수를 입력하세요 > '))

if data6 < 0:
    print(-1)
else:
    result = 0
    while data6 > 0:
        result += data6 % 10
        data6 //= 10
    else:
        print(result)
        

# solution 3

num = int(input())
sum = 0

if num < 0:
    sum = -1
else:
    while num > 0:
        sum += num%10
        num = int(num/10)

print(sum) 