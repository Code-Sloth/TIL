# 1547 공 https://www.acmicpc.net/problem/1547

ball = 1
for _ in range(int(input())):
    a,b = map(int,input().split())
    if ball == a:ball = b
    elif ball == b:ball = a
print(ball)

# 5576 콘테스트 https://www.acmicpc.net/problem/5576

print(sum(sorted([int(input()) for i in range(10)])[-3:]),
      sum(sorted([int(input()) for i in range(10)])[-3:]))

# 2846 오르막길 https://www.acmicpc.net/problem/2846

n = int(input())
li = list(map(int,input().split()))

li_t,t = [],0
for i in range(n-1):
    if li[i+1] > li[i]:
        t += (li[i+1] - li[i])
    else:
        li_t.append(t)
        t = 0
li_t.append(t)

print(max(li_t))

# 1251 단어 나누기 https://www.acmicpc.net/problem/1251

s = input().rstrip()
n = len(s)
li = []

for i in range(1,n-1):
    for j in range(i+1,n):
        li.append(s[:i][::-1]+s[i:j][::-1]+s[j:][::-1])

print(sorted(li)[0])