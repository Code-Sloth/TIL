# SQL - Nested Queries

<br/>

## Subquery
- 단일 쿼리문에 여러 테이블의 데이터를 결합하는 방법
- ex) table1에서 가장 나이가 어린 사람을 삭제?
```sql
SELECT MIN(age)
FROM table1;
--    +
DELETE FROM table1
WHERE age = 위에서 찾은 최소값;
--    =
DELETE FROM table1
WHERE age = (
  SELECT MIN(age) FROM table1
)
```
- 특징
  - 조건에 따라 하나 이상의 테이블에서 데이터를 검색하는 데 사용
  - SELECT, FROM, WHERE, HAVING 절 등에서 다양한 맥락에서 사용
- FROM 절에 서브쿼리 생성 가능 / AS로 별칭 꼭 지어줘야 함
- INNER JOIN 절에서 ON 대신 USING 사용 가능 / 같은 COLUMN일 때

<br/>

## EXISTS
- 쿼리 문에서 반환된 레코드의 존재 여부를 확인
```sql
SELECT
  select_list
FROM
  table
WHERE
  [NOT] EXISTS (subquery);
```
- subquery가 하나 이상의 행을 반환하면 EXISTS 연산자는 true를 반환하고 그렇지 않으면 false를 반환
- 주로 WHERE 절에서 subquery의 반환 값 존재 여부를 확인하는데 사용

<br/>

## CASE
- SQL문에서 조건문을 구성
```sql
CASE case_value
  WHEN when_value1 THEN statements
  WHEN when_value2 THEN statements
  ...
  [ELSE else-statements]
END CASE;
```
- case_value가 when_value와 동일한 것을 찾을 때까지 순차적으로 비교
- when_value와 동일한 case_value를 찾으면 해당 THEN 절의 코드를 실행
- 동일한 값을 찾지 못하면 ELSE절의 코드를 실행
  - ELSE절이 없을 때 동일한 값을 찾지 못하면 오류 발생

<br/>

### SQL 문제 사이트
[HackerLank](https://www.hackerrank.com/)