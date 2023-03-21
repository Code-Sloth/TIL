# 파일 입출력

<br/>

### **`파일 입력`**

- open('file', mode = 'r', encoding = 'UTF8')
- with open('file', mode = 'w', encoding = 'UTF8') as f:

<br/>

## JSON

- json은 자바스크립트 객체 표기법으로 개발환경에서 많이 활용되는 데이터 양식으로 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용함
- 문자 기반(txt) 데이터 포멧으로 다수의 프로그래밍 환경에서 쉽게 활용 가능
  - 텍스트를 언어별 데이터 타입으로 변환시키거나
  - 언어별 데이터 타입을 적절하게 텍스트로 변환

<br/>

### **`JSON 파일의 활용`**

- 객체(리스트, 딕셔너리 등)을 json으로 변환
  ```python
  import json
  json.dumps(x)
  ```
- json을 객체로 변환
  ```python
  x = json.load(f)
  ```

<br/>

### **`pprint`**

- 임의의 파이썬 데이터 구조를 보기좋게 프린트
  ```python
  from pprint import pprint
  ```