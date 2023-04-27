# 2493 탑
# 109864KB / 412ms

n = int(input())
g = [0] + list(map(int,input().split())) # 인덱스 1이 첫번째 수가 되도록 만듦
result = [0] * (n+1) # 마찬가지로 1이 첫번째 수

for right in range(2, n+1):
    left = right-1          # left = 1, right 2부터 탐색
    while left:             # left가 첫번째 수까지 탐색되도록 반복
        if g[left] >= g[right]:         # 왼쪽 탑이 오른쪽 탑보다 크면
            result[right] = left        # 오른쪽 탑에 왼쪽 탑의 인덱스를 저장
            break
        else:                           # 크지않으면
            left = result[left]         # 왼쪽 탑의 신호를 받는 더 왼쪽의 탑부터 탐색

print(' '.join(map(str,result[1:])))

'''
ex) 입력
10
1 2 3 10 2 3 4 6 9 10

                g
1   2   3   10  2   3   4   6   8   10
              result
0   0   0   0   4   4   4   4   4   4

상황)
left = 8 (6)
right = 9 (8)

else:
    left = result[8]

left = 4 (10) 부터 다시 탐색
중간에 필요없는 2 3 4 과정 생략
'''