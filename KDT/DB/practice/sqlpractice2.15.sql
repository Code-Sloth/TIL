-- 문제 1
-- 테이블 employees 과 테이블 offices 를 officeCode 기준으로 INNER JOIN 한 데이터를 조회하시오.
-- employeeNumber, lastName, firstName, city 필드만 조회하시오.
-- employeeNumber 기준 오름차순으로 정렬하세요.
SELECT
	employeeNumber,
    lastName,
    firstName,
    city
FROM employees as t1
INNER JOIN offices as t2
	ON t1.officeCode = t2.officeCode
ORDER BY
	employeeNumber;

-- 문제 2
-- 테이블 customers 와 테이블 offices 를 city 기준으로 LEFT JOIN 한 데이터를 조회하시오.
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.
SELECT
	customerNumber,
    officeCode,
    t1.city,
    t2.city
FROM customers as t1
LEFT JOIN offices as t2
	ON t1.city = t2.city
ORDER BY customerNumber DESC;

-- 문제 3
-- 테이블 customers 와 테이블 offices 를 city 기준으로 RIGHT JOIN 한 데이터를 조회하시오.
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.
SELECT
	customerNumber,
    officeCode,
    t1.city,
    t2.city
FROM customers as t1
RIGHT JOIN offices as t2
	ON t1.city = t2.city
ORDER BY customerNumber DESC;

-- 문제 4
-- 테이블 customers 와 테이블 offices 를 city 기준으로 INNER JOIN 한 데이터를 조회하시오.
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.
SELECT
	customerNumber,
    officeCode,
    t1.city,
    t2.city
FROM customers as t1
INNER JOIN offices as t2
	ON t1.city = t2.city
ORDER BY customerNumber DESC;

-- 문제 5
-- 문제 2, 문제 3, 문제 4 의 조회 결과가 다른 이유를 작성하시오.
-- INNER JOIN은 city가 겹치는 데이터들 모두를 불러온다.
-- LEFT JOIN은 city가 같은 데이터들과 왼쪽 테이블의 모든 레코드를 불러온다.
-- RIGHT JOIN은 city가 같은 데이터들과 오른쪽 테이블의 모든 레코드를 불러온다.

-- 문제 6
-- 테이블 customers 와 테이블 offices 를 city 기준으로 FULL OUTER JOIN 한 데이터를 조회하시오.
-- MySQL에서 FULL OUTER JOIN 은 지원하지 않는 기능이므로 MySQL FULL OUTER JOIN 키워드를 검색하여 구현하시오.
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.
SELECT
	customerNumber,
    officeCode,
    t1.city,
    t2.city
FROM
	customers as t1
LEFT JOIN offices as t2
	ON t1.city = t2.city
UNION
SELECT
	customerNumber,
    officeCode,
    t1.city,
    t2.city
FROM
	customers as t1
RIGHT JOIN offices as t2
	ON t1.city = t2.city
ORDER BY customerNumber DESC;

-- 문제 7
-- 테이블 orderdetails 와 테이블 orders 를 INNER JOIN 한 데이터를 조회하시오.
-- orderNumber , orderDate 필드만 조회하시오.
-- orderNumber 기준 오름차순으로 정렬하세요.
SELECT
	orderNumber,
    orderDate
FROM orderdetails
NATURAL JOIN orders
ORDER BY orderNumber;

-- 문제 8
-- 테이블 orderdetails 와 테이블 products 을 INNER JOIN 한 데이터를 조회하시오.
-- orderNumber , productCode , productName 필드만 조회하시오.
-- orderNumber 기준 오름차순으로 정렬하세요.
SELECT
	orderNumber,
    productCode,
    productName
FROM orderdetails
NATURAL JOIN products
ORDER BY orderNumber;

-- 문제 9
-- 테이블 orderdetails , 테이블 orders , 테이블 products 를 INNER JOIN 한 데이터를 조회하시오.
-- orderNumber , productCode , orderDate, productName 필드만 조회하시오.
-- orderNumber 기준 오름차순으로 정렬하세요.
SELECT
	orderNumber,
    productCode,
    orderDate,
    productName
FROM orderdetails
NATURAL JOIN (orders,products)
ORDER BY orderNumber;
