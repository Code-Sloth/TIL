# String

<br/>

## 목록
|번호|명령어|설명|
|--|--------|----------------------------------------------------|
|1|**s.count(a,i,j)**|s에서 a의 개수?|
|2|**s.find(a,i,j)**|s에서 a의 위치?|
|3|**s.upper, s.lower()**|s를 대문자, 소문자로 변환|
|4|**s.strip()**|s의 공백, 개행문자를 제거|
|5|**s.replace(a,b,n)**|s의 a문자를 b로 교체|
|6|**s.startswith(a), s.endswith(a)**|s의 시작,끝이 a문자열?|
|7|**s.translate**|s의 문자를 t를 이용해 a를 b로 바꿈|
|8|**s.split(a)**|s의 문자열을 a를 기준으로 구분|
|9|**a.join(s)**|s의 문자열을 a를 기준으로 결합|
|10|**print(s+a), print(s*i)**|s에 문자열을 a와 합침,i만큼 반복출력|

<br/>

```python
🌈 s.count(a,i,j)
s의 i부터 j전까지 인덱스 중 a의 개수를 반환

s = 'Hello World!'
print(s.count('l',1,7))
# 2
```

```python
🌈 s.find(a,i,j) , s.index(a,i,j)
s의 i부터 j전까지 인덱스 중 첫 a의 인덱스를 반환
a가 s에 존재하지 않으면 find는 -1 을 반환, index는 error 발생

s = 'Hello World!'
print(s.find('l',1,7))
print(s.index('b',0,8))
# 2
# ValueError: substring not found
```

```python
🌈 s.upper() , s.lower()
s 문자열을 대문자 , 소문자로 변환

s = 'Hello World!'
print(s.upper())
print(s.lower())
# HELLO WORLD!
# hello world!
```

```python
🌈 s.strip() , s.lstrip() , s.rstrip()
s의 양쪽 , 왼쪽 , 오른쪽의 공백이나 개행문자를 제거

s = ' Hello World!\n '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
# Hello World!
# Hello World!
# 
#  Hello World!
```

```python
🌈 s.replace(a,b,n)
s의 a문자를 b로 n번 바꿔줌

s = 'Hello World!'
print(s.replace('l','y',2))
# Heyyo world!
```

```python
🌈 s.startswith(a) , s.endswith(a)
s의 시작, 끝이 a문자열이면 True or False

s = 'Hello World!'
print(s.startswith('He'))
print(s.endswith('hey'))
# True
# False
```

```python
🌈 t = str.maketrans(a,b)
s = s.translate(t)
s의 문자를 t(a:b 1대1 대응관계)를 이용해 a를 b로 바꿔줌

s = 'a2b4c6d8'
t = str.maketrans('abcd','1357')
s = s.translate(t)
print(s)
# 12345678
```

```python
🌈 s.split(a)
s의 문자열을 a를 기준으로 구분

s = 'He!llo! World'
print(s.split('!'))
# ['He', 'llo', 'World']
```

```python
🌈 a.join(s)
s의 문자열들을 a를 기준으로 결합

s = 'He','llo','World'
print('!'.join(s))
# He!llo!World
```

```python
🌈 print(s+a) , print(s*i)
파이썬에서는 문자열을 더하거나 곱할 수 있음

s = 'Hello World!'
a = ' Hi World!'
i = 3
print(s+a)
print(s*i)
# Hello World! Hi World!
# Hello World!Hello World!Hello World!  
```