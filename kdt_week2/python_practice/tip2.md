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

- 