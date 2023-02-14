-- 문제 1
-- 필드 정보를 참고해서 테이블 users 를 생성하시오.
CREATE TABLE users(
	userId int auto_increment,
    first_name varchar(20) not null,
    last_name varchar(20) not null,
    birthday date not null,
    city varchar(100),
    country varchar(100),
    email varchar(100),
    created_at datetime default CURRENT_TIMESTAMP,
    PRIMARY KEY (userId)
);

-- 문제 2
-- 레코드 정보를 보고 테이블 users 에 데이터를 입력하시오.
INSERT INTO	
	users(first_name, last_name, birthday, city, country, email)
VALUES
	('Beemo','Jeong','1000-01-01',NULL,NULL,'beemo@hqhk.kr'),
    ('Jieun','Lee','1993-05-16','Seoul','Korea',NULL),
    ('Dami','Kim','1995-04-09','Seoul','Korea',NULL),
    ('Kwangsoo','Lee','1985-07-14','Seoul','Korea',NULL);

-- 문제 3
-- 테이블 users 에 임의로 데이터 5개를 입력하시오.
INSERT INTO
	users(first_name, last_name, birthday, city, country, email)
VALUES
	('minsu1','2','1996-01-22','4','5','6'),
    ('minsu2','8','1996-02-22','10','11','12'),
    ('minsu3','14','1996-03-22','16','17','18'),
    ('minsu4','20','1996-04-22','22','23','24'),
    ('minsu5','26','1996-05-22','28','29','30');

-- 문제 4
-- 2번 레코드의 first_name, last_name, birthday 필드 값을 자신의 이름, 성, 생년월일로 변경하시오.
UPDATE
	users
SET	
	first_name = 'Minwook',
    last_name = 'Lee',
    birthday = '1996-08-22'
WHERE
	userId = 2;

-- 문제 5
-- 테이블 users 에서 country 필드가 NULL 인 모드 레코드의 country 필드 값을 Korea 로 변경하시오.
UPDATE
	users
SET
	country = 'Korea'
WHERE
	country IS NULL;

-- 문제 6
-- 테이블 users 에서 first_name 필드가 Beemo 인 레코드를 삭제하시오.
DELETE FROM
	users
WHERE
	first_name = 'Beemo';

-- 문제 7
-- 테이블 users 에서 first_name 필드가 Kwangsoo, last_name 필드가 Lee 인 레코드를 삭제하시오.
DELETE FROM
	users
WHERE
	first_name = 'Kwangsoo' and last_name = 'Lee';

-- 문제 8
-- 테이블 users 에서 가장 나중에 생성한 레코드 1개를 삭제하시오.
DELETE FROM
	users
ORDER BY
	created_at DESC
LIMIT 1;
