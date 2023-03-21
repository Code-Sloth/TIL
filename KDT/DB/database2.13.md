# SQL - Single Table Queries 2

<br/>

## Filtering data
- Clause
  - DISTINCT
  - WHERE
  - LIMIT
- Operator
  - BETWEEN
  - IN
  - LIKE
  - Comparison
  - Logical

<br/>

### DISTINCT
- 중복 값을 제거
- SELECT 키워드 바로 뒤에 작성

<br/>

### WHERE
- 조회 시 특정 검색 조건을 지정 (파이썬에서 if문)
- FROM 키워드 뒤에 위치
- =, !=, >, <, AND, OR, NOT 등등 가능
- 사이 값은 AND로 두번 비교 or BETWEEN AND 사용
- record IN (1,3,4) : 1 또는 3 또는 4이면 , NOT IN도 가능
- LIKE '%son' : son으로 끝나는 데이터들
- LIKE '___y' : 4자리면서 y로 끝나는 데이터들

<br/>

### LIMIT
- LIMIT [offset,] row_count;
- 하나 또는 두 개의 인자를 사용 (0 또는 양의 정수)
- row_count는 조회할 최대 레코드 수를 지정
- 순서는 ORDER BY 뒤에 옴
- ex) LIMIT 3,5 : 4번째부터 8번째까지 (offset 처음 값은 0) = LIMIT 5 OFFSET 3

<br/>

## Grouping

<br/>

### GROUP BY
- 레코드를 그룹화하여 요약본 생성 with 집계 함수
- SUM, AVG, MAX, MIN, COUNT
- FROM, WHERE 뒤에 배치
- WHERE는 그룹 전 HAVING은 그룹 후 조건문

<br/>

## SELECT statement 문법 작성 순서
- SELECT - FROM - WHERE - GROUP BY - HAVING - ORDER BY - LIMIT

<br/>

## SELECT statement 실행 순서
- FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY - LIMIT
1. FROM : 테이블에서
2. WHERE : 특정 조건에 맞춰
3. GROUP BY : 그룹화 하고
4. HAVING : 만약 그룹 중에서 조건이 있다면 맞추고
5. SELECT : 조회하여
6. ORDER BY : 정렬하고
7. LIMIT : 특정 위치의 값을 가져온다

<br/>

#### 정렬에서의 NULL
- MySQL에서 NULL은 NULL이 아닌 값 앞에 위치
  - NULL값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력
- WHERE 문에 Table IS NOT NULL 로 NULL값을 없앤다