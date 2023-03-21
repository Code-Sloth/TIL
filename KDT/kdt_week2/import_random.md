# Import Random

- 랜덤 모듈

<br/>

## 목록
|번호|명령어|설명
|--|-----|------|
|1|**import random**|random모듈 import|
|2|**random.random()**|0~1 사이 랜덤 실수|
|3|**random.uniform(i,j)**|i~j 사이 랜덤 실수|
|4|**random.randint(i,j)**|i~j 사이 랜덤 정수|
|5|**random.randrange(i,j,k)**|i~j k스텝 랜덤 정수|
|6|**random.choice(seq)**|seq안의 랜덤 요소|
|7|**random.sample(seq,i)**|seq안의 i개의 랜덤 요소|
|8|**random.shuffle(seq)**|seq을 랜덤으로 정렬|

<br/>

```python
🌈 import random
random 모듈을 import
```

```python
🌈 random.random()
0~1 사이의 랜덤 실수를 리턴

print(random.random())
# 0.0724827885209729
```

```python
🌈 random.uniform(i,j)
i와 j사이의 랜덤 실수를 리턴

print(random.uniform(1,10))
# 4.429699973020678
```

```python
🌈 random.randint(i,j)
i와 j사이의 랜덤 정수를 리턴

print(random.randint(1,10))
# 7
```

```python
🌈 random.randrange(i,j,k)
i와 j사이의 k스텝 랜덤 정수를 리턴

print(random.randrange(1,10,2))
# 5
```

```python
🌈 random.choice(seq)
seq안에서 랜덤하게 하나의 요소를 반환

a = [1,2,3,'a','b','c']
print(random.choice(a))
# b
```

```python
🌈 random.sample(seq,i)
seq안의 여러개의 랜덤 요소를 반환

a = [1,2,3,'a','b','c']
print(random.sample(a,3))
# [2,1,'b']
```

```python
🌈 random.shuffle(seq)
seq안의 순서를 랜덤하게 바꿈

a = [1,2,3,'a','b','c']
random.shuffle(a)
print(a)
# ['c', 'a', 'b', 1, 3, 2]
```