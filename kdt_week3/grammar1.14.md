# 추가 문법

###  **`조건 표현식 (Conditional Expression)`**

```python
num = 3
a = num if num >=0 else -num
print(a)
# 3

num = -3
a = num if num >=0 else -num
print(a)
# 3
====================================================
# 다음 두 개의 코드는 같음
num = 2
if num % 2:
  a = '홀'
else:
  a = '짝'
print(a)

num = 2
a = '홀' if num % 2 else '짝'
print(a)
```

### **`Enumerate 순회`**

```python
mems = ['민수','영희','철수']

for i in range(len(mems)):
  print(f'{i} {mems[i]}')
# 0 민수
# 1 영희
# 2 철수

for i, mems in enumerate(mems):
  print(i, mems)
# 0 민수
# 1 영희
# 2 철수

enumerate(mems)
print(list(enumerate(mems)))
# [(0,'민수'),(1,'영희'),(2,'철수')]
```

### **`List Comprehension`**

```python
# 다음 두 개의 코드는 같음
li = []
for nums in range(1,4):
  li.append(nums**3)
print(li)
# [1, 8, 27]

print([nums**3 for nums in range(1,4)])
# [1, 8, 27]
```

### **`Dictionary Comprehension`**

```python
# 다음 두 개의 코드는 같음
di = {}
for nums in range(1,4):
  di[nums] = nums ** 3
print(di)
# {1: 1, 2: 8, 3: 27}

print({nums:nums**3 for nums in range(1,4)})
# {1: 1, 2: 8, 3: 27}
```

### **`Lambda`**

```python
# 다음 두 개의 코드는 같음
def func(a,b):
  return a + b
print(func(2,3))

print((lambda a,b : a + b)(2,3))
# 5
====================================================
                  List Lambda
li = [1,2,3,4,5,6,7,8,9]

li_map = map(lambda i : i*a, li)
# 요소를 하나씩 넣어 리턴된 값으로 새로운 리스트 생성
li_fil = filter(lambda i : i%2==0, li)
# 요소를 넣어 리턴 값이 참인 것만 리스트에 추가

print(li,list(li_map),list(li_fil),sep='\n')
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# [2, 4, 6, 8]
====================================================
               List Sorted Lambda
li = [['b',3],['a',5],['c',1],['d',4]]

print(sorted(li,key=lambda i:i[0]))
print(sorted(li,key=lambda i:i[1]))
# [['a', 5], ['b', 3], ['c', 1], ['d', 4]]
# [['c', 1], ['b', 3], ['d', 4], ['a', 5]]
====================================================
              Dictionary Sorted Lambda
di = {'b':3,'a':5,'c':1,'d':4}

# items는 튜플로 저장
1. 첫번째 요소 기준으로 정렬
2. 두번째 요소 기준으로 정렬
print(sorted(di.items(),key=lambda i:i[0]))
print(sorted(di.items(),key=lambda i:i[1]))
# [('a', 5), ('b', 3), ('c', 1), ('d', 4)]
# [('c', 1), ('b', 3), ('d', 4), ('a', 5)]

1. 첫번째 요소 기준으로 거꾸로 정렬
2. 두번째 요소 기준으로 거꾸로 정렬
print(sorted(di.items(),key=lambda i:i[0],reverse=True))
print(sorted(di.items(),key=lambda i:i[1],reverse=True))
# [('d', 4), ('c', 1), ('b', 3), ('a', 5)]
# [('a', 5), ('d', 4), ('b', 3), ('c', 1)]

1. key 순서대로 key를 정렬
2. key 순서대로 key를 거꾸로 정렬
print(sorted(di,key=lambda i:i))
print(sorted(di,key=lambda i:i,reverse=True))
# ['a', 'b', 'c', 'd']
# ['d', 'c', 'b', 'a']

1. value 순서대로 key를 정렬
2. value 순서대로 key를 거꾸로 정렬
print(sorted(di,key=lambda i:di[i]))
print(sorted(di,key=lambda i:di[i],reverse=True))
# ['c', 'b', 'd', 'a']
# ['a', 'd', 'b', 'c']

1. value가 높은 순서로 2명 정렬
2. value가 낮은 순서로 2명 정렬
di = {'b':3,'a':5,'c':1,'d':4}
print(sorted(di,key=lambda i:di[i])[:2])
print(sorted(di,key=lambda i:di[i],reverse=True)[:2])
# ['c', 'b']
# ['a', 'd']

1. value가 높은 순서로 value를 정렬
2. value가 낮은 순서로 value를 정렬
print(sorted(di.values(),key=lambda i:i))
print(sorted(di.values(),key=lambda i:i,reverse=True))
# [1, 3, 4, 5]
# [5, 4, 3, 1]
```

## API dotenv 설정

```python
1. 터미널 창에 pip install python-dotenv 입력해서 설치

2. .env 파일에 원하는 값을 입력
ex) apikey = '1567423181234153asdf156asdf'

3. .gitignore 파일에 .env 추가

4. apikey를 입력할 파일에 import 추가 및 실행
ex) from dotenv import load_dotenv
    import os
    load_dotenv()

5. 원하는 변수에 apikey 변수 설정
ex) api_key = os.environ.get('apikey')

# 주의 사항
5번의 apikey와 .env에 설정한 apikey가 같아야 함
```