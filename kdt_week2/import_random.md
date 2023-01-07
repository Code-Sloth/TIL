# Import Random

- 랜덤 모듈

<br/>

## 목록
- random.random()
- random.uniform(i,j)
- random.randint(i,j)
- random.randrange(i,j,k)
- random.choice(seq)
- random.sample(seq)
- random.shuffle(seq)

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
🌈 random.sample(seq)
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