# CLI (Command Line Interface)

<br/>

## 정의

<br/>


- **`가상 가상 터미널 또는 텍스트 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식`**
- **`GUI(Graphic User Interface) = 그래픽기반의 인터페이스
CLI(Command Line Interface) = 명령어기반의 인터페이스`**

<br/>


## 기초 파일시스템 명령어

<br/>


- ### **`(cd) change directory 디렉토리 이동`**
```
cd b

b라는 폴더로 이동 

cd ..

상위 폴더로 이동
```

<br/>

- ### **`(ls) list 목록`**
```
ls

파일 및 폴더 확인
```

<br/>

- ### **`(mkdir) make directory 디렉토리 생성`**
```
mkdir 'b'

b라는 폴더를 생성
```

<br/>

- ### **`(touch) 파일 생성`**
```
touch a.txt

a라는 텍스트 파일을 생성
```

<br/>

- ### **`(rm) remove 파일이나 폴더 삭제`**
```
rm a.txt

a라는 파일 삭제

rm -r b

b라는 폴더를 삭제 (폴더 안 파일까지 삭제)
```

<br/>

- ### **`문제 예시`**
```
CLI 명령어를 활용하여 7반의 1번 본인 이름.txt를 생성



$ git init

$ cd cli

$ mkdir '7반'

$ cd 7반

$ mkdir '1'

$ cd 1

$ touch 이민욱.txt

$ ls
이민욱.txt
```
<br/>
<br/>

# Git (분산 버전 관리 시스템)

## 정의

<br/>

- **`리누스 토르발스가 개발하였으며 코드의 버전을 관리하는 도구`**
- **`컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 파일들의 작업을 조율`**
- **`중앙집중식버전관리시스템 = 로컬에서 편집하고 중앙 서버에서 버전관리 분산버전관리시스템 = 로컬에서도 버전관리, 원격저장소를 활용하여 협업`**

<br/>

## Git 버전 관리 기초

<br/>

1. **`작업을 하고`**
2. **`변경된 파일을 모아 (add)`**
3. **`버전으로 남긴다. (commit)`**

<br/>

## Git 기본 명령어

- ### **`git init`**
```
git init

git 폴더가 생성
```

<br/>

- ### **`git add`**
```
git add report.txt

working directory에 있는 report라는 파일을 staging area에 추가
```

<br/>

- ### **`git commit -m`**
```
git commit -m 'report'

staged 상태의 report 파일을 커밋을 통해 버전으로 기록
```

<br/>

- ### **`git status`**
```
git status

Git 저장소에 있는 파일의 상태를 확인
- nothing to commit = working directory가 비어있음
- working tree clean = staging area가 비어있음
```

<br/>

- ### **`git log`**
```
git log

현재 저장소에 기록된 커밋을 조회
```

<br/>

## Git 명령어 이해

<br/>

![Git 구조](https://user-images.githubusercontent.com/121420601/209784583-3ecc2055-1e3c-457c-9e8e-377efa008c6c.png)