# Dictionary

- mutable, iterable
- key(immutable만 가능), value(둘 다 가능) 쌍을 요소로 갖는 자료형
- key는 중복을 허용하지 않음
- 반복문에서 기본적으로 key를 순회

<br/>

## 목록
|번호|명령어|설명
|----|-----|-----|
|1|**a[k]=b**|a에 k(key), b(value)추가|
|2|**del a[k]**|a의 k요소 삭제|
|3|**print(a[k]**|a의 k의 value값 출력|
|4|**k in a**|a에 k(key)가 있는지 확인|
|5|**a.items, list(a.items())**|a를 다른 객체, list로 변환|
|6|**for k in a**|a의 k(key)를 다 불러옴|
|7|**for k,v in a.items()**|a의 k(key),v(value)값을 다 불러옴|
|8|**a.clear**|a의 모든 항목 제거|
|9|**a.copy**|a를 복사|
|10|**a.get(k,i)**|a의 k(key)의 value를 반환, 없으면 i를 반환|
|11|**a.update(b)**|a에 b를 추가 / key가 있으면 value값 교체|
|12|**a.pop(k,i)**|a의 k(key)의 value를 반환 후 제거, 없으면 i를 반환|


<br/>

```python
🌈 a[k] = b
a딕셔너리에 k라는 key와 b라는 value를 추가

a = {'a': 1, 'b' : 2, 'c' : 3}
a['d'] = 4
print(a)
# {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4}
```

```python
🌈 del a[k]
a딕셔너리의 k라는 key 요소 삭제

a = {'a': 1, 'b' : 2, 'c' : 3}
del a['b']
print(a)
# {'a': 1, 'c' : 3}
```

```python
🌈 print(a[k])
a딕셔너리에서 k(key)의 value값 출력

a = {'a': 1, 'b' : 2, 'c' : 3}
print(a['b'])
# 2
```

```python
🌈 k in a
a 딕셔너리에 k라는 key가 있는지 확인

a = {'a': 1, 'b' : 2, 'c' : 3}
print('a' in a)
# True
```

```python
🌈 a.keys() , a.values() , a.items()
list(a.keys()) , list(a.values()), list(a.items())
a 딕셔너리를 key,value,둘 다의 객체들로 변환
a 딕셔너리를 list로 변환

a = {'a': 1, 'b' : 2, 'c' : 3}
b = a.keys()
c = a.values()
d = a.items()
print(b,c,d,sep='\n')
# dict_keys(['a', 'b', 'c'])
# dict_values([1, 2, 3])     
# dict_items([('a', 1), ('b', 2), ('c', 3)])

a = {'a': 1, 'b' : 2, 'c' : 3}
b = list(a.keys())
c = list(a.values())
d = list(a.items())
print(b,c,d,sep='\n')
# ['a','b','c']
# [1,2,3]
# [('a',1), ('b',2), ('c',3)]
```

```python
🌈 for key in a:
      print(key,a[key])
a 딕셔너리의 key를 반복문으로 불러옴

a = {'a': 1, 'b' : 2, 'c' : 3}
for k in a:
  print(k,a[k])
# a 1
# b 2
# c 3
```

```python
🌈 for key,value in a.items():
      print(key,value)
items를 활용해 a 딕셔너리의 key와 value를 반복문으로 불러옴

a = {'a': 1, 'b' : 2, 'c' : 3}
for k,v in a.items():
  print(k,v)
# a 1
# b 2
# c 3
```

```python
🌈 a.clear()
a 딕셔너리의 모든 항목을 제거

a = {'a': 1, 'b' : 2, 'c' : 3}
a.clear()
print(a)
# {}
```

```python
🌈 a.copy()
a 딕셔너리를 복사

a = {'a': 1, 'b' : 2, 'c' : 3}
b = a.copy()
print(b)
# {'a': 1, 'b' : 2, 'c' : 3}
```

```python
🌈 a.get(k,i)
a 딕셔너리의 k라는 key의 value를 반환, 없으면 i를 반환

a = {'a': 1, 'b' : 2, 'c' : 3}
print(a.get('a','not in'))
print(a.get('d','not in'))
# 1
# not in
```

```python
🌈 a.update(b)
a딕셔너리에 b딕셔너리를 추가 / key가 존재하면 value값을 교체

a = {'a': 1, 'b' : 2, 'c' : 3}
b = {'d': 4}
a.update(b)
print(a)
# {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4}
```

```python
🌈 a.pop(k,i)
a에 k(key)가 있으면 해당 값을 반환 후 제거, 없으면 i를 반환
해당 key가 없을 때 i를 입력하지 않으면 KeyError

a = {'a': 1, 'b' : 2, 'c' : 3}
print(a.pop('a','error!!'))
print(a.pop('d'))
print(a.pop('d','error!!'))
# 1
# keyerror: 'd'
# error!!
```