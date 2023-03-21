# MySQL Guide

<br/>

## Workbench 활용 MySQL 접속 방법
1. sample database 다운로드
2. MySQL 접속, Local Instance 클릭
3. Administration -> Data Import/Restore
4. Import from Self-Contained File 체크 -> ...클릭 -> sample파일 선택 후 Start Import
5. Schemas 클릭 -> 새로고침 -> classicmodels 확인

<br/>

## 실습 데이터베이스에 대한 쿼리(Query)문 작성 및 쿼리문 실행 방법
1. classicmodels 선택
2. Query 에디터 클릭
3. 쿼리문 입력
```
SELECT * FROM customers;
```
4. 전기 모양 실행버튼 클릭
5. 출력 확인
