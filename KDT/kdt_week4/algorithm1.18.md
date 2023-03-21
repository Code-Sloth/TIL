# 문자열 알고리즘

<br/>

## 문자열

<br/>

- immutable

<br/>

### 문자열 조작

<br/>

```python
s = 'abcdefghi'
s[2:5] - 'cde'
s[-6:-2] - 'defg'
s[2:5:2] - 'ce'
s[-6:-1:3] - 'dg'
s[2:5:-1] - ''
```

<br/>

### 문자열 메서드

<br/>

- [문자열 메서드 정리 깃허브](https://github.com/Code-Sloth/TIL/blob/master/kdt_week2/string.md)

<br/>

## 아스키(ASCII) 코드

<br/>

- 알파벳을 표현하는 대표 인코딩 방식
- 각 문자를 표현하는데 1byte(8bits) 사용
- ord(문자 -> 아스키 코드)
- chr(아스키 코드 -> 문자)
