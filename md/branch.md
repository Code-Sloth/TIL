# Branch

<br/>

## 정의

<br/>

- **`독립적인 작업흐름을 만들고 관리하며 커밋 사이를 이동하는 어떤 포인터`**


<br/>

## 주요 명령어

<br/>

- ### **`git branch []`**
```
git branch [branch name]

브랜치를 생성
```

<br/>

- ### **`git checkout []`**
```
git checkout [branch name]

[]안의 브랜치로 이동
```

<br/>

- ### **`git checkout -b []`**
```
git checkout -b [branch name]

[]안의 브랜치를 생성하고 이동
```

<br/>


- ### **`git branch`**
```
git branch

브랜치의 목록 확인
```

<br/>


- ### **`git branch -d []`**
```
git branch -d [branch name]

[]안의 브랜치를 삭제
```

<br/>


- ### **`git merge[]`**
```
git merge [branch name]

[]안의 브랜치와 현재 브랜치를 병합
- fast-foward = 브랜치 생성된 이후 master 브랜치에 변경사항이 없음
```

<br/>

![mergeimage](https://raw.githubusercontent.com/Code-Sloth/TIL/master/image/mergeimage.png)

<br/>

- ### **`상황 1`**
```
touch readme.md > 내용 작성
git branch test   ┐  = git checkout -b test
git checkout test ┘
touch a.md > 내용 작성
git add .
git commit -m 'testtest'
git checkout master
git merge test
git branch -d test

master에서 변경 사항이 없으므로 자동 병합
병합 완료
```

<br/>

- ### **`상황 2`**
```
touch readme.md > 내용 작성
git add .
git commit -m 'readme'
git checkout -b test
touch a.md > 내용 작성
git add .
git commit -m 'a'
git checkout master
touch b.md > 내용 작성
git add .
git commit -m 'b'
git merge test
git branch -d test

test와 master에서 서로 다른 파일을 수정했으므로 충돌 없이
병합 완료
```

<br/>

- ### **`상황 3`**
```
touch readme.md > 내용 작성
git add .
git commit -m 'readme'
git checkout -b test
readme 내용 수정
git add .
git commit -m 'a'
git checkout master
readme 내용 수정
git add .
git commit -m 'b'
git merge test
충돌 내용 선택 및 정리
git add .
git commit -m 'update readme'
git branch -d test

같은 파일이라 충돌이 일어나지만 합의점을 찾아 수정 후
병합 완료
```

<br/>

# GitHub Flow 기본 원칙

<br/>

1. master branch는 반드시 배포 가능한 상태(완성된 코드)여야 한다.
2. feature branch는 각 기능의 의도를 알 수 있도록 작성한다. (이름 알기쉽게) 
3. Commit message는 매우 중요하며, 명확하게 작성한다. (알기 쉽게 커밋 이름 설정)
4. Pull Request를 통해 협업을 진행한다.
5. 변경사항을 반영하고 싶다면, master branch에 병합한다.

<br/>

## GitHub Flow Models

<br/>

- ### **`Shared Repository Model`**
```
1. 상대방의 초대 수락
2. git clone
3. 독립적인 branch 생성 후 작업
4. Commit으로 작업의 history를 남김
5. 원격 저장소에 push
6. Github에서 Pull Request
7. 상대가 Code Review 후 Merge
```

<br/>

- ### **`Fork & Pull Model`**
```
1. Github에서 상대의 원격 저장소를 fork
2. fork한 내 저장소를 git clone
3. 이후 과정은 Shared Repository Model과 동일
```
