# SQL - Advanced 01

<br/>

## Transactions
- 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법
- ex) 계좌이체
  - 중간에 문제가 발생한다면 거래를 처음부터 없었던 거래로 만들어야 함
```sql
START TRANSACTION;
state_ments;
...
[ROLLBACK|COMMIT]
```
- START TRANSACTION : 트랜잭션 구문의 시작
- COMMIT : 모든 작업이 정상적으로 완료되면 한꺼번에 DB에 반영
- ROLLBACK : 부분적으로 작업이 실패하면 트랜잭션에서 진행한 모든 연산을 취소하고 실행전으로 되돌림

### TRANSACTION Practice
```sql
SET autocommit = 0;

CREATE TABLE users (
  id INT AUTO_INCREMENT,
  name VARCHAR(10) NOT NULL,
  PRIMARY KEY (id)
)

START TRANSACTION;

INSERT INTO users (name)
VALUES ('james'), ('mary');

SELECT * FROM users;

ROLLBACK; /// COMMIT;

SELECT * FROM users
```
- 쪼개질 수 없는 업무처리의 단위
- 전체가 수행되거나 또는 전혀 수행되지 않아야 함(All or Nothing)

<br/>

## Triggers
- 특정 이벤트에 대한 응답으로 자동으로 실행되는 것
```sql
CREATE TRIGGER trigger_name
  {BEFORE | AFTER} {INSERT|UPDATE|DELETE}
  ON table_name FOR EACH ROW
  trigger_body;
```
- CREATE TRIGGER키워드 다음에 생성하려는 트리거의 이름을 지정
- 각 레코드의 어느 시점에 트리거가 실행될지 지정
- ON 키워드 뒤에 트리거가 속한 테이블의 이름을 지정
- 트리거가 활성화될 때 실행할 코드를 trigger body에 지정
  - 여러 명령문을 실행하려면 BEGIN END키워드로 묶어서 사용
- BEGIN END 사이에 다중 구문을 구성 가능
- DELIMITER // : 종료 문구를 //로 바꿈
- OLD / NEW : 전의 데이터 or 새로운 
  - INSERT : NEW
  - UPDATE : OLD, NEW
  - DELETE : OLD

<br/>

### Triggers 추가 명령문
```sql
SHOW TRIGGERS; -- 트리거 목록 확인
DROP TRIGGER trigger_name; -- 트리거 삭제
```

<br/>

### Trigger 생성 시 에러 해결
```sql
-- 실행중인 프로세스 목록 확인
SELECT * FROM information_schema.INNODB_TRX;

-- 특정 프로세스의 trx_mysql_thread_id 삭제
KILL [trx_mysql_thread_id1];
```

<br/>

### 실습 코드
```sql
DROP TABLE users;

SET autocommit = 0;

CREATE TABLE users (
  id INT AUTO_INCREMENT,
  name VARCHAR(10) NOT NULL,
  PRIMARY KEY (id)
);

START TRANSACTION;

INSERT INTO users (name)
VALUES ('james'), ('mary');

SELECT * FROM users;

-- ROLLBACK;
COMMIT;

SELECT * FROM users;

DROP TABLE articles;

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createAt DATETIME NOT NULL,
    updateAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO articles (title, createAt, updateAt)
VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articles;

DELIMITER //
CREATE TRIGGER myTrigger
	BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
	SET NEW.updateAt = CURRENT_TIME();
END //
DELIMITER ;

SHOW TRIGGERS;

UPDATE articles
SET title = 'new title'
WHERE id = 1;

SELECT * FROM articles;

CREATE TABLE articleLogs (
	id INT AUTO_INCREMENT,
    description VARCHAR(100) NOT NULL,
    createAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER recordLogs
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogs (description, createAt)
    VALUES (CONCAT(NEW.id,'번 글이 작성 되었습니다.'), CURRENT_TIME());
END//
DELIMITER ;

DROP TRIGGER recordLogs;
SHOW TRIGGERS;

SELECT * FROM articles;

INSERT INTO articles (title, createAt, updateAt)
VALUES ('title3', CURRENT_TIME(), CURRENT_TIME());

SELECT * FROM articleLogs;

CREATE TABLE backUpArticles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createAt DATETIME NOT NULL,
    updateAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER backUpLogs
	AFTER DELETE
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO backUpArticles (title, createAt, updateAt)
    VALUES (OLD.title, OLD.createAt, OLD.updateAt);
END //
DELIMITER ;

SHOW TRIGGERS;

DELETE FROM articles
WHERE id = 1;

SELECT * FROM backupArticles;
```