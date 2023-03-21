# SQL-Managing Tables / DDL

<br/>

## CREATE TABLE
- 각 필드에 적용할 데이터 타입 작성
- 테이블 및 필드에 대한 제약조건 작성
```sql
CREATE TABLE examples (
  examId INT AUTO_INCREMENT,
  lastName VARCHAR(50) NOT NULL,
  firstName VARCHAR(50) NOT NULL,
  PRIMARY KEY (examId)
);
-- 테이블 구조 확인
SHOW COLUMNS FROM examples;
```
- INT, VARCHAR(50) : 데이터 타입 / CHAR 고정길이, VARCHAR 가변길이
- NOT NULL, PRIMARY KEY : 제약 조건
- AUTO_INCREMENT : 속성

<br/>

### 대표적인 MySQL Data Types
- Numeric : 숫자형 : INT, FLOAT, ...
- String : 문자형 : VARCHAR, TEXT, ...
- Date and Time : DATE, DATETIME, ...
- 필요할 때 찾아서 사용

<br/>

### 제약 조건 Constraint
- 데이터 무결성을 지키기 위해 데이터를 입력 받을 때 실행하는 검사 규칙
- 대표적인 MySQL Constraints
  - PRIMARY KEY : 해당 필드를 기본 키로 지정
  - NOT NULL : 해당 필드에 NULL값을 저장하지 못하도록 지정

<br/>

### AUTO_INCREMENT attribute
- 테이블의 기본 키에 대한 번호 자동 생성
- 기본 키 필드에 사용
  - 고유한 숫자를 부여
- 시작 값은 1이며 데이터 입력 시 값을 생략하면 자동으로 1씩 증가
- 이미 사용한 값을 재사용하지 않음
- 기본적으로 NOT NULL 제약 조건을 포함

<br/>

## DELETE a Table
- 테이블 삭제
```sql
DROP TABLE table_name;
```

<br/>

## Modifying table fields

<br/>

### ALTER TABLE statement
- 테이블 필드 조작
- ALTER TABLE ADD : 필드 추가
- ALTER TABLE MODIFY : 필드 속성 변경
- ALTER TABLE CHANGE COLUMN : 필드 이름 변경
- ALTER TABLE DROP COLUMN : 필드 삭제
```sql
ALTER TABLE
  table_name
(ADD, MODIFY, CHANGE COLUMN, DROP COLUMN)
  new_column_name column_definition;
```
- CHANGE COLUMN은 old_column_name new_column_name column_definition
- 속성, 이름 둘 다 변경할 시 CHANGE COLUMN만 사용 가능

<br/>

### 참고
- 반드시 NOT NULL 제약을 사용해야되는 건 아님
- 데이터베이스를 사용하늩 프로그램에 따라 NULL을 저장할 필요가 없는 경우가 많으므로 되도록이면 NOT NULL로 정의
- 값이 없다라는 표현을 테이블에 기록하는 것은 0이나 빈 문자열 등을 사용하는 것으로 대체하는 것을 권장

<br/>

# SQL - Modifying Data - DML

<br/>

## INSERT statement
- 테이블 레코드 삽입
```sql
INSERT INTO table_name (c1,c2,...)
VALUES (v1,v2,...)
```
- INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록을 작성
- VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록을 작성

<br/>

### 예제 테이블 생성
```sql
CREATE TABLE articles(
  id INT AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL,
  PRIMARY KEY (id)
);
```

<br/>

## Update data in table
- 테이블 레코드 수정
```sql
UPDATE table_name
SET column_name = expression,
[WHERE
  condition];
```
- SET절 다음에 수정 할 필드와 새 값을 지정
- WHERE절에서 수정 할 레코드를 지정하는 조건 작성 (ex WHERE id = 1;)
  - WHERE절을 작성하지 않으면 모든 레코드 수정하니 주의
- REPLACE(clumn_name, old_name, new_name) 문자열 대체

<br/>

## Delete data from table
- 테이블 레코드 삭제
```sql
DELETE FROM table_name
[WHERE
  condition];
```
- DELETE FROM절 다음에 테이블 이름 작성
- WHERE절에서 삭제할 레코드를 지정하는 조건 작성

<br/>

### 전체 실습 코드
```sql
CREATE TABLE examples (
    examId INT AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    PRIMARY KEY (examId)
);
-- 테이블 구조 확인
SHOW COLUMNS FROM examples;

DROP TABLE examples;

ALTER TABLE
	examples
ADD
	country VARCHAR(100) NOT NULL;

ALTER TABLE
	examples
ADD age INT NOT NULL,
ADD address VARCHAR(100) NOT NULL;

ALTER TABLE
	examples
MODIFY
	address VARCHAR(50) NOT NULL;

ALTER TABLE
	examples
MODIFY lastName VARCHAR(10) NOT NULL, 
MODIFY firstName VARCHAR(10) NOT NULL;

ALTER TABLE
	examples
CHANGE COLUMN
	country state VARCHAR(100) NOT NULL;

SHOW COLUMNS FROM examples;

ALTER TABLE
	examples
DROP COLUMN
	address;
    
ALTER TABLE
	examples
DROP COLUMN	state,
DROP COLUMN age;

CREATE TABLE articles(
  id INT AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL,
  PRIMARY KEY (id)
  );
SHOW COLUMNS FROM articles;

INSERT INTO 
	articles(title, content, createdAt)
VALUES
	('hello','world','2000-01-01');

INSERT INTO 
	articles(title, content, createdAt)
VALUES
	('title1','content1','1900-01-01'),
    ('title2','content2','1800-01-01'),
    ('title3','content3','1700-01-01');

SELECT * FROM articles;

INSERT INTO
	articles(title, content, createdAt)
VALUES
	('mytitle', 'mycontent', CURDATE());
    
UPDATE articles 
SET 
    title = 'newTitle'
WHERE
    id = 1;

UPDATE articles
SET 
	title = 'newTitle1',
    content = 'newContent1'
WHERE
	id = 2;
    
SELECT * FROM articles;

SET sql_safe_updates=0;

UPDATE
	articles
SET
	content = REPLACE(content, 'content', 'TEST');

DELETE FROM
	articles
WHERE
	id = 1;

DELETE FROM
	articles
ORDER BY
	createdAt DESC
LIMIT 2;
```