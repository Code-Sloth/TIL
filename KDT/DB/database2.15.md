# SQL - Multi Table Queries

<br/>

## Join
- 둘 이상의 테이블에서 데이터를 검색하는 방법
- INNER JOIN
- OUTER JOIN
  - LEFT JOIN
  - RIGHT JOIN
- CROSS JOIN

<br/>

### INNER JOIN
- 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
```sql
SELECT
  select_list
FROM
  table1
INNER JOIN table2
  ON table1.fk = table2.pk;
```
- FROM절 이후 메인 테이블 지정
- INNER JOIN절 이후 메인 테이블과 조인할 테이블을 지정
- ON키워드 이후 조인 조건을 작성
  - 조인 조건은 table1과 table2간의 레코드를 일치시키는 규칙을 지정

### LEFT JOIN
- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
```sql
SELECT
  select_list
FROM
  table1
LEFT [OUTER] JOIN table2
  ON table1.fk = table2.pk;
```
- FROM절 이후 왼쪽 테이블 지정
- LEFT JOIN절 이후 오른쪽 테이블 지정
- ON키워드 이후 조인 조건을 작성
  - 왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴
- 특징
  - 왼쪽은 무조건 표시하고, 매치되는 레코드가 없으면 NULL을 표시
  - 왼쪽 테이블 한 개의 레코드에 여러 개의 오른쪽 테이블 레코드가 일치할 경우,
  해당 왼쪽 레코드를 여러 번 표시

<br/>

### RIGHT JOIN
- 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드 반환
```sql
SELECT
  select_list
FROM
  table1
RIGHT [OUTER] JOIN table2
  ON table1.fk = table2.pk;
```
- FROM절 이후 왼쪽 테이블 지정
- RIGHT JOIN절 이후 오른쪽 테이블 지정
- ON키워드 이후 조인 조건을 작성
  - 오른쪽 테이블의 각 레코드를 왼쪽 테이블의 모든 레코드와 일치시킴
- 특징
  - 오른쪽은 무조건 표시하고, 매치되는 레코드가 없으면 NULL을 표시
  - 오른쪽 테이블 한 개의 레도크에 여러 개의 왼쪽 테이블 레코드가 일치할 경우, 해당 오른쪽 레코드를 여러 번 표시

<br/>

### 정리
![joinimage](https://raw.githubusercontent.com/Code-Sloth/TIL/master/image/joinimage.png)

<br/>

### 실습 코드

```sql
DROP TABLE articles;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(100) NOT NULL,
    userId INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO
	users (name)
VALUES
	('권미자'),
    ('류준하'),
    ('정영식');

INSERT INTO
	articles (title, content, userId)
VALUES
	('제목1', '내용1', 1),
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 4);

SELECT
	productCode,
    productName
FROM products
INNER JOIN productlines
	ON products.productLine = productlines.productLine;

SELECT
	t1.orderNumber,
    t1.status
FROM orders as t1
INNER JOIN orderdetails as t2
	ON t1.orderNumber = t2.orderNumber;
    
SELECT
	t1.orderNumber,
    t1.status,
    SUM(quantityOrdered * priceEach) AS totalSales
FROM orders AS t1
INNER JOIN orderdetails AS t2
	ON t1.orderNumber = t2.orderNumber
GROUP BY orderNumber;

SELECT
	*
FROM
	articles
LEFT JOIN users
	ON articles.userId = users.id;
    
SELECT
	contactFirstName,
    orderNumber,
    status
FROM
	customers as t1
LEFT JOIN orders as t2
	ON t1.customerNumber = t2.customerNumber;

SELECT
	contactFirstName,
    orderNumber,
    status
FROM
	customers as t1
LEFT JOIN orders as t2
	ON t1.customerNumber = t2.customerNumber
WHERE t2.orderNumber IS NULL;

SELECT
	*
FROM
	articles
RIGHT JOIN users
	ON articles.userId = users.id;

SELECT
	employeeNumber,
    firstName,
    customerNumber,
    contactFirstName
FROM
	customers
RIGHT JOIN employees
	ON salesRepEmployeeNumber = employeeNumber;

SELECT
	employeeNumber,
    firstName,
    customerNumber,
    contactFirstName
FROM
	customers
RIGHT JOIN employees
	ON salesRepEmployeeNumber = employeeNumber
WHERE salesRepEmployeeNumber IS NULL;
```