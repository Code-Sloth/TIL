# 함수

<br/>

## 함수 기본 구조

- 선언과 호출(Define & Call)
- 입력(Input)
- 범위(Scope)
- 결과값(Output)

<br/>

### **`선언과 호출`**

- 함수의 선언 def
- 들여쓰기
- 함수는 Parameter로 넘겨줄 수 있음
- 함수는 동작 후에 return을 통해 결과값을 전달

```python
n1 = 0
n2 = 1

def f1(a,b):
  return a+b
def f2(a,b):
  return a-b
def f3(a,b):
  return f1(a,5) + f2(5,b)
sol = f3(n1,n2)
print(sol)
# 9
```

<br/>

### **`함수의 결과값`**

- 함수는 반드시 하나의 값만 return
- return과 동시에 실행 종료

<br/>

### **`함수의 입력`**

- Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
- Argument : 함수를 호출할 때, 넣어주는 값

```python
def func(ham): # parameter : ham
  return ham

func('spam') # argument : 'spam'
```

- 직접 변수의 이름으로 특정 Argument를 전달 가능
- Keyword Argument 다음에 Positional Argument는 활용 불가

```python
def abc(a,b,c):
  return b,a,c

abc(1,2,c=3)
# (2,1,3)
abc(1,b=2,3)
# SyntaxError
```

<br/>

### **`함수의 범위`**

- 함수는 코드 내부에 local scope 외의 공간에 global scope
- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scope : 함수가 만든 scope 함수 내부에서만 참조 가능

<br/>

### **`함수 이해 image`**

![함수 이해 image](https://raw.githubusercontent.com/Code-Sloth/TIL/master/kdt_week3/image/func.png)