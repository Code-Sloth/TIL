# list 총 정리

<br/>

- ### mutable / iterable
- ### sequence(데이터에 순서가 있는 것) (list, tuple, range, string)

<br/>

## 목록
|번호|명령어|설명|
|--|--------|----------------------------------------------------|
|1|**len(a)**|요소가 몇 개?|
|2|**a[n]**|요소의 위치?|
|3|**a[i:j]**|i부터 j까지 요소 씀|
|4|**c in a**|c가 a안에?|
|5|**a.count(b)**|a안에 b가 몇 개?|
|6|**a.index(b)**|a에서 b의 위치?|
|7|**a.append(b)**|a에 b를 추가|
|8|**a.extend(b)**|a에 b안의 요소를 하나씩 추가|
|9|**a.insert(i,b)**|a의 i번째에 b를 추가|
|10|**a.pop()**|a의 마지막 요소를 뺌|
|11|**a.pop(b)**|a의 b번째 요소를 뺌|
|12|**del a[i]**|a의 i번째 요소를 삭제|
|13|**a.sort()**|a를 순서대로 정렬|
|14|**sorted(a)**|정렬된 a를 불러옴|
|15|**max(a) , min(a)**|a의 최댓값 , 최솟값|
|16|**a.reverse()**|a의 순서를 뒤집음|
|17|**''.join(a)**|''안의 구분자를 넣으며 a의 요소들을 합침|
|18|**a.copy()**|a를 복사|

<br/>

```python
🌈 len(a)
전체 요소 개수를 리턴

a = [1,2,3,'a','b','c']
print(len(a))
# 6
```

```python
🌈 a[n]
특정 인덱스 i의 요소를 가져옴

a = [1,2,3,'a','b','c']
print(a[3])
# a
```

```python
🌈 a[i:j]
범위 i이상 j미만까지 요소를 가져옴

a = [1,2,3,'a','b','c']
print(a[2:5])
# 3 a b
```

```python
🌈 c in a
c요소가 a안에 있는지 확인

c = 'a'
a = [1,2,3,'a','b','c']
print(c in a)
# True
```

```python
🌈 a.count(b)
b요소가 a안에 몇 개 있는지 확인

b = 'a'
a = [1,2,3,'a','b','c','a']
print(a.count(b))
# 2
```

```python
🌈 a.index(b)
b요소의 위치 파악

b = 'b'
a = [1,2,3,'a','b','c']
print(a.index(b))
# 4
```

```python
🌈 a.append(b)
a리스트에 b요소를 마지막에 추가 / 통째로 넣음

b = 'qwer'
a = [1,2,3,'a','b','c']
a.append(b)
print(a)
# [1,2,3,'a','b','c','qwer']
```

```python
🌈 a.extend(b)
a리스트에 b안의 요소들을 마지막에 병합 / 요소 하나씩 넣음

b = 'qwer'
a = [1,2,3,'a','b','c']
a.extend(b)
print(a)
# [1,2,3,'a','b','c','q','w','e','r']
```

```python
🌈 a.insert(i,b)
a리스트의 i번 index로 b를 추가 / 통째로 넣음

b = 'd'
a = [1,2,3,'a','b','c']
a.insert(1,b)
print(a)
# [1,'d',2,3,'a','b','c']
```

```python
🌈 a.pop()
a리스트의 마지막 요소를 빼서 반환

a = [1,2,3,'a','b','c']
print(a.pop())
print(a)
# c
# [1,2,3,'a','b']
```

```python
🌈 a.pop(b)
a리스트의 b번째 요소를 빼서 반환

a = [1,2,3,'a','b','c']
print(a.pop(1))
print(a)
# 2
# [1,3,'a','b','c']
```

```python
🌈 del a[i]
a리스트의 i번째 요소를 삭제

a = [1,2,3,'a','b','c']
del a[2]
print(a)
# [1,2,'a','b','c']
```

```python
🌈 a.sort()
a리스트를 순서대로 정렬 / a자체가 바뀜

a = ['d','e','z','b','a','c']
a.sort()
print(a)
# ['a','b','c','d','e','z']
```

```python
🌈 sorted(a)
정렬된 a리스트로 반환 / a자체가 바뀌진 않음

a = [4,5,2,3,7,6,1]
print(sorted(a))
print(a)
# a = [1,2,3,4,5,6,7]
# a = [4,5,2,3,7,6,1]
```

```python
🌈 max(a) , min(a)
a리스트의 최댓값과 최솟값을 반환

a = [2,1,6,10,5,3,-1]
print(max(a), min(a))
# 10 -1
```

```python
🌈 a.reverse()
리스트의 순서를 뒤집음

a = [1,2,3,'a','b','c']
a.reverse()
print(a)
# ['c','b','a',3,2,1]
```

```python
🌈 ''.join(a)
''사이의 구분자를 요소사이마다 넣으며 문자열을 합침

b=[]
a = ['a','b','c']
b.append(''.join(a))
print(b)
# ['abc']
```

```python
🌈 a.copy()
a리스트를 복사한다 / b = a로 하면 a에도 'd'가 추가됨

a = [1,2,3,'a','b','c']
b = a.copy()
b.append('d')
print(b)
print(a)
# [1,2,3,'a','b','c','d']
# [1,2,3,'a','b','c']
```

