import sys
sys.stdin = open('input.txt', 'r')

import string as ss

s = input().upper() # 문자열을 대문자로 받는다
abc = ss.ascii_uppercase # abc변수에 대문자 문자열을 받는다
li = [] # li 리스트 생성
print(abc)
for a in abc: # 모든 대문자를 하나씩 넣어본다
    li.append(s.count(a)) # 입력받은 s문자열에 a가 몇개있는지 리스트로 저장
    b = li.index(max(li)) # li 리스트의 최댓값 인덱스를 b에 저장
print(li)
print(b)
if max(li) not in li[b+1:]: # 최댓값이 li의 최댓값인덱스 다음부터 없으면
    print(abc[b]) # 대문자 집합 문자열에서 최댓값 b의 인덱스의 값을 출력
else:
    print('?')

# import ~~ as s d