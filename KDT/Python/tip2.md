# 1.2~ Tip

- 나눠서 입력받기
```
num9,num10,num11,num12,num13 = map(int,input().split())
print(num9+num10+num11+num12+num13)
# map과 split으로 정수형을 입력받을 수 있음

a,b=map(int,input().split())
print(a+b, a-b, a*b, a%b,sep="\n")
# sep = '\n' 지정하면 알아서 줄바꿈

## 백준 2588
#sol1
a=int(input())
b=int(input())
c=b%10
d=(b-(b//100)*100)//10
e=b//100
print(a*c,a*d,a*e,a*b,sep='\n')

#sol2
a = input()
b = input()
a=int(a)
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))
```

- ALT누르면 여러줄 한번에 입력 가능
- Shift Tap 첫줄로 이동
- 
```
num = int(input())

if num%2==1:
    print('홀수')
else:
    print('짝수')

num = int(input())

if num%2:
    print('홀수')
else:
    print('짝수')
# True 가 1이니까 동일한 코드

dust =int(input())
if 0 <= dust <= 30:
    print('좋음')
elif 30 < dust <= 80:
    print('보통')
elif 80 < dust <= 150:
    print('나쁨')
elif 151 < dust:
    print('매우나쁨')
else:
    print('양의 정수를 입력하세요.')

# elif dust <= 80 만 입력해도 된다.

# step
range(0,-6,-1)
```

- python tutor 사이트 참고
- 
```
a = 'pineapple'
# 반복 가능한 객체 : 각 요소가 필요할 때
for i in range(len(a)):
    print(a[i])
# 반복 가능한 객체 : 인덱스가 필요할 때
for char in a:
    print(char)
```

- print(char, end='') / 출력 이어지게 함
- 
```
word = 'banana'

# a를 만나면 1을 출력하고 종료하세요.
for char in word:
    if char == 'a':
        print(1)
        break
    
print('=============')
# a를 제외하고 모두 출력하세요.
for char in word:
    if char == 'a':
        print(1)
        continue
```

- 알고리즘 문제 풀 때 시간 단축을 위해 쓰는 명령어
```
import sys # 사전 입력
input() 대신에 아래 명령어 대신 입력
sys.stdin.readline()
```

- 1부터 입력받은 정수까지의 합
```
a=int(input())
n=0
i=1

while i<=a:
    n += i
    i += 1

print(n)
=====================================
n=0
for i in range(1,int(input())+1):
    n += i
print(n)
=====================================

print(sum(range(1,int(input())+1)))
```

- 
```
c=int(input())

for i in range(1,c+1):
    for j in range(i):
        print('*',end='')
    print('')
```

- a.pop() : a의 마지막 요소를 삭제한다.
- 개행 이해 / print()에는 기본적으로 end가 개행이 담겨있다.
```
print('-')
print()
print()
print('-')

print('-')
print('\n')
print('\n')
print('-')

print('-')
print('\n',end='')
print('\n',end='')
print('-')
```

- 리스트 입력 받기 (아직 이해 x)
```
numList = list(map(int, number_list[1:-1].split(',')))
# [1, 2, 3, 4, 5]를 입력받았다고 치면
string = input()
numList = list(map(int, string[1:-1].split(',')))
```

- while True: 무한 루프
- while 문에서 다른 입력을 했을 때 코드가 종료되게 해준다
```
while True:
    try:
        a,b=map(int,input().split())
    except:
        break
    print(a+b)
```

- print(b.count(c)) // b에서 c가 몇개 있는지 확인
- [내장함수 정리 사이트](https://docs.python.org/ko/3/library/functions.html#aiter)
- 리스트 대괄호 빼고 출력
```
b = [1, 2, 3, 4, 5]

print(b) # [1, 2, 3, 4, 5]
print(*b) # 1 2 3 4 5
```
- 리스트 인덱스
```
a = [1, 4, 2, 7, 3]

print(a.index(max(a))+1)

# 4
```
- [list 관련 정보](https://wikidocs.net/14)

- [파이썬 기본 튜토리얼](https://www.w3schools.com/python/default.asp)
- remove : 특정 색인이 아닌 첫번째 일치 값을 제거
- del : 특정 인덱스에서 항목을 제거
- pop : 특정 인덱스에서 항목을 제거하고 값을 반환
```
a = [1, 2, 3, 4]
b = 4
a.remove(b)
# 1, 2, 3
del a[1]
# 2, 3, 4
a.pop(1)
# 2
```

- 최댓값 최솟값 구할 때 초기값을 0이 아닌 원소의 첫번째 값으로 설정
```
max = nums[0]
```

- [코드업 사이트](https://codeup.kr/problemsetsol.php?psid=33) - 문제, 문제집, python 기초 100제

- 딕셔너리에 바로 입력값 저장
```
d = {}
b = []

for j in range(3):
    b.append(input())

for i in b:
    d[i] = input('')

for key,value in d.items():
    print(key,value,sep=' : ')
```

- [list, dictionary 정리 사이트](https://wikidocs.net/86293)

- 초기화의 위치 중요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
- 반복문 안에 둬야 하는지 맨 위에 둬야 하는지!!!!!!!!!!!!!!!!!!!