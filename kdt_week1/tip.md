# Tip

- CLI -> 불편한 것이 아니라 전혀 다르게 생각하고 조작하자.
- git add b 탭키를 누르면 blahblah라는 폴더가 자동으로 입력
- 파일이나 폴더 이름은 영어로 짓고 공백은 _로 교체
- q = quick 터미널 명령창 안에서 나가기
- git log --oneline 한줄로 간단히 나타냄
- gitignore 이미 commit한 경우엔 무시를 안해서 미리 설정해야함
- 삭제해도 삭제했다는 commit은 남아있음
- 메모장은 글씨가 깨진다.

<br/>

- fatal: refusing to merge unrelated histories 오류 해결법

https://jobc.tistory.com/177

해결 명령어 : git pull origin main --allow-unrelated-histories

- 질문 하기 전에 구글링하며 생각해보고 질문하기 / 코드 오류 메세지 확인
- 커밋과 저장은 다른 개념이다
- b.txt를 잘못 add했을 때 git restore --staged b.txt
- 커밋 제목 수정 코드 git commit --amend / 하지만 해시값이 달라지기 때문에 push한 이후에는 amend X

- 폴더 이름 수정 git mv (현재폴더이름) (바꿀폴더이름) /// 폴더이름 소문자로만 써야함!

- 마크 다운 이모지 윈도우키 + .

- 나눠서 입력받기
```
num9,num10,num11,num12,num13 = map(int,input().split())
print(num9+num10+num11+num12+num13)
# map과 split으로 정수형을 입력받을 수 있음

a,b=map(int,input().split())
print(a+b, a-b, a*b, a%b,sep="\n")
# sep = '\n' 지정하면 알아서 줄바꿈

## 백준 2588
#sol1
a=int(input())
b=int(input())
c=b%10
d=(b-(b//100)*100)//10
e=b//100
print(a*c,a*d,a*e,a*b,sep='\n')

#sol2
a = input()
b = input()
a=int(a)
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))
```

- 