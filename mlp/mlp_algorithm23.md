# 그리디

<br/>

## 그리디 알고리즘
- 탐욕법으로 현재 상황에서 지금 당장 좋은 것만 고르는 방법
- 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
- 정당성 분석이 중요
  - 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토

<br/>

### 예시
- 루트 노드부터 시작하여 거쳐 가는 노드 값의 합을 최대로 만들고 싶을 때
  - 단순히 매 상황에서 가장 큰 값만 고른다면 최적의 해를 보장할 순 없음
  - 하지만 코딩테스트에서의 대부분의 그리디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있어야 풀리도록 출제
- 이코테 거스름 돈 문제
  - 시간 복잡도 O(K)
- 이코테 1이 될 때까지 문제
- 이코테 곱하기 혹은 더하기 문제
- 이코테 모험가 길드 문제

<br/>

### 이코테 모험가 길드 문제
- 모험가 N명, 공포도 X
- 공포도 X인 모험가는 반드시 X명 이상으로 구성된 무험가 그룹에 참여
- 최대 몇 개의 모험가 그룹을 만들 수 있는 지
- 단, 모험을 떠나지 않아도 됨
```python
n = int(input())
data = list(map(int,input().split()))
data.sort()
result,count = 0,0

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)
```