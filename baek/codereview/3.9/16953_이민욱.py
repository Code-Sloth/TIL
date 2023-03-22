# 16953 A -> B
# 31256KB / 52ms

import sys
input = sys.stdin.readline

a,b = map(int,input().split())

def dfs(a,t):
    if a > b:return # 수를 넘어가면 return하고 다시 dfs
    if a == b: print(t); sys.exit() # 같아지면 멈춤
    dfs(a*2,t+1) # 곱하기 2
    dfs(a*10+1,t+1) # 오른쪽에 1 추가

dfs(a,1) # 최솟값에 1을 더한 값을 출력해야 함
print(-1)