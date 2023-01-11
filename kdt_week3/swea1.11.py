import sys
sys.stdin = open('input.txt','r')

# 2047. 신문 헤드라인

print(input().upper())

# 2025. N줄덧셈

print(sum(list(range(1,int(input())+1))))

# 1936 1대1 가위바위보

a,b = map(int,input().split())

if b-a == 1 or b-a == -2:
    print('B')
else:
    print('A')

# 2027. 대각선 출력하기

for i in range(5):
    for j in range(5):
        if i==j:
            print('#',end='')
        else:
            print('+',end='')
    print()

# 2058. 자릿수 더하기

print(sum(list(map(int,input()))))

# 2019. 더블더블

for i in range(int(input())+1):
    print(int(2**i),end=' ')