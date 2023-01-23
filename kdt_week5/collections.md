# Collections



- Counter

```python
import Counter

from collections import Counter
s = 'abbcccddddeeeee'
di_s = Counter(s)
print(di_s)
# Counter({'e': 5, 'd': 4, 'c': 3, 'b': 2, 'a': 1})

from collections import Counter
s = [1,1,1,1,2,2,2,3,3,4]
di_s = Counter(s)
print(di_s)
# Counter({1: 4, 2: 3, 3: 2, 4: 1})
print(di_s.most_common(2))
# [(1, 4), (2, 3)]
```

- update()

```python
import collections

a = collections.Counter()
print(a)
a.update('abcdefg')
print(a)
a.update({'f':3, 'e':2})
print(a)
# Counter()
# Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1})     
# Counter({'f': 4, 'e': 3, 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1})
```

- elements()

```python
import collections

a = collections.Counter('Hello Python')
print(list(a.elements()))
print(sorted(a.elements()))
# ['H', 'e', 'l', 'l', 'o', 'o', ' ', 'P', 'y', 't', 'h', 'n']
# [' ', 'H', 'P', 'e', 'h', 'l', 'l', 'n', 'o', 'o', 't', 'y']

b = collections.Counter(a=4,b=2,c=0,d=-2)
print(sorted(b.elements()))
# ['a', 'a', 'a', 'a', 'b', 'b']
```

- subtract()

```python
import collections
a = collections.Counter('hello python')
b = collections.Counter('i love python')
a.subtract(b)
print(a)
# Counter({'h': 1, 'l': 1, 'e': 0, 'o': 0, 'p': 0, 'y': 0, 't': 0, 'n': 
# 0, ' ': -1, 'i': -1, 'v': -1}) 

c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
# Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

# 덧셈, 뺄셈, 교집합, 합집합 다 가능
```

### deque, defaultdict 등등 나중에 추가