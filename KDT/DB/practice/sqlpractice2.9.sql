-- 문제 1
-- 테이블 employees 에서 모든 데이터를 조회하시오.
SELECT
	*
FROM
	employees;

-- 문제 2
-- 테이블 customers 에서 customerNumber , customerName , phone 필드의 모든 데이터를 조회하시오.
SELECT
	customerNumber,
    customerName,
    phone
FROM
	customers;

-- 문제 3
-- 테이블 employees 에서 firstName , lastName , email 필드의 모든 데이터를 조회하시오.
-- 단, firstName 기준 오름차순으로 정렬하세요.
SELECT
	firstName,
    lastName,
    email
FROM
	employees
ORDER BY
	firstName;
    
-- 문제 4
-- 테이블 employees 에서 firstName , lastName , email 필드의 모든 데이터를 조회하시오.
-- firstName 필드는 이름 , lastName 필드는 성 , email 필드는 이메일 로 출력하세요.
-- 이름 기준 오름차순으로 정렬하세요.
SELECT
	firstName '이름',
    lastName '성',
    email '이메일'
FROM
	employees
ORDER BY
	firstName;
    
-- 문제 5
-- 테이블 employees 에서 employeeNumber , lastName , firstName , officeCode , jobTitle 필드의 모든 데이터를 조회하시오.
-- 단, jobTitle 기준 내림차순 officeCode 기준 내림차순으로 정렬하세요.
SELECT
	employeeNumber,
    lastName,
    firstName,
    officeCode,
    jobTitle
FROM
	employees
ORDER BY
	jobTitle DESC,
    officeCode DESC;
    
-- 문제 6
-- 테이블 orderdetails 에서 모든 데이터를 조회하시오.
-- 단, quantityOrdered 기준 오름차순 priceEach 기준 오름차순으로 정렬하세요.
SELECT
	*
FROM
	orderdetails
ORDER BY
	quantityOrdered,
    priceEach;
    
-- 문제 7
-- 테이블 customers 에서 customerNumber , country , contactFirstName 필드의 모든 데이터를 조회하시오.
-- 단, country 기준 오름차순 contactFirstName 기준 내림차순으로 정렬하세요.
SELECT
	customerNumber,
    country,
    contactFirstName
FROM
	customers
ORDER BY
	country,
    contactFirstName DESC;
    
-- 문제 8
-- 테이블 products 에서 productCode , quantityInStock , buyPrice 그리고 quantityInStock * buyPrice 필드의 모든 데이터를 조회하시오.
-- 단, quantityInStock * buyPrice 기준 내림차순으로 정렬하세요.
SELECT
	productCode,
    quantityInStock,
    buyPrice,
    quantityInStock * buyPrice
FROM
	products
ORDER BY
	quantityInStock * buyPrice DESC;