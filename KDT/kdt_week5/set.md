# 세트

<br/>

- ### 집합 (합,교,차 등등 연산 가능)
- ### 중복을 허용하지 않고 순서를 보장하지 않음(인덱스 x)
- ### 특정 값이 있는지 확인하는 방법(in)

<br/>

## 목록
|번호|명령어|설명|
|--|--------|----------------------------------------------------|
|1|**se = set([iterable])**|세트 생성|
|2|**se\|se2**|합집합|
|3|**se&se2**|교집합|
|4|**se-se2**|차집합|
|5|**se^se2**|대차집합|
|6|**se >= se2**|부분집합|
|7|**se.add(a)**|se에 a추가|
|8|**se.update([])**|se에 여러요소 추가|
|9|**se.remove(a),se.discard(a)**|se에서 a요소 삭제(에러o,x)|
|10|**se.pop()**|se의 임의요소 삭제 후 반환|
|11|**se.clear()**|se 모든 요소 삭제|
|12|**len(se)**|se의 길이|
|13|**se.copy()**|se의 세트 복사|


<br/>

```python
🌈 se = {1,2} , se = set([iterable])
세트 생성
```

```python
🌈 se | se2
se와 se2의 합집합

se = {'a','b','c','d','e'}
se2 = {'d','e','f','g','h'}
print(se | se2)
# {'g', 'h', 'd', 'a', 'c', 'b', 'e', 'f'} 
```

```python
🌈se & se2
se와 se2의 교집합

se = {'a','b','c','d','e'}
se2 = {'d','e','f','g','h'}
print(se & se2)
# {'e', 'd'}
```

```python
🌈se - se2
se와 se2의 차집합

se = {'a','b','c','d','e'}
se2 = {'d','e','f','g','h'}
print(se - se2)
# {'c', 'a', 'b'}
```

```python
🌈se ^ se2
se와 se2의 대차집합

se = {'a','b','c','d','e'}
se2 = {'d','e','f','g','h'}
print(se ^ se2)
# {'b', 'h', 'a', 'f', 'g', 'c'}
```

```python
🌈 se > se2 , se >= se2
se2가 se의 진부분집합인지 , se2가 se의 부분집합인지

se = {'a','b','c','d','e'}
se2 = {'a','b','c','d','e'}
print(se > se2)
print(se >= se2)
# False
# True
```

```python
🌈 se.add(a)
se에 a요소를 추가

se = {'a','b','c','d','e'}
se.add('f')
print(se)
# {'e', 'b', 'a', 'd', 'c', 'f'}
```

```python
🌈 se.update([a,b,c.....])
se에 여러 요소들을 한번에 추가

se = {'a','b','c','d','e'}
se.update(['f','g','h','i'])
print(se)
# {'d', 'h', 'f', 'g', 'i', 'a', 'e', 'c', 'b'}
```

```python
🌈 se.remove(a) , se.discard(a)
둘 다 se의 요소 삭제 , remove는 에러 발생 dicard는 에러 x

se = {'a','b','c','d','e'}
se.remove('b')
se.discard('f')
print(se)
# {'e', 'd', 'c', 'a'}
```

```python
🌈 se.pop()
se에서 임의의 요소를 삭제하고 반환, 에러 o

se = {'a','b','c','d','e'}
print(se.pop())
print(se)
# e
# {'c', 'b', 'a', 'd'}
```

```python
🌈 se.clear()
se의 모든 요소 삭제

se = {'a','b','c','d','e'}
se.clear()
print(se)
# set()
```

```python
🌈 len(se)
se의 길이 반환

se = {'a','b','c','d','e'}
print(len(se))
# 5
```

```python
🌈 se2 = se.copy()

se = {'a','b','c','d','e'}
se2 = se.copy()
print(se2)
# {'b', 'c', 'a', 'd', 'e'}
```
