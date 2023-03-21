# 10817 세 수 https://www.acmicpc.net/problem/10817

h = list(map(int,input().split()))
print(sorted(h)[1])

# 20001 고무오리 디버깅 https://www.acmicpc.net/problem/20001

from collections import deque
q = deque()

if input().strip() == '고무오리 디버깅 시작':
    while 1:
        s = input().strip()
        if s == '고무오리 디버깅 끝':break
        elif s == '고무오리':
            if not q:
                q.append('문제')
                q.append('문제')
            else:q.pop()
        elif s == '문제':
            q.append(s)
    print('고무오리야 사랑해') if not q else print('힝구')

# 1269 대칭 차집합 https://www.acmicpc.net/problem/1269

n, m = map(int,input().split())
a = set(list(map(int,input().split())))
b = set(list(map(int,input().split())))

print(len(a^b))

# 3052 나머지 https://www.acmicpc.net/problem/3052

se = set()
for i in range(10):
    se.add(int(input())%42)
print(len(se))

# 1181 단어 정렬 https://www.acmicpc.net/problem/1181

se = set()
for _ in range(int(input())):
    s = input().strip()
    se.add((s,len(s)))

se = sorted(se,key = lambda x:x[0])
se = sorted(se,key = lambda x:x[1])

for i in range(len(se)):
    print(se[i][0])

# sol 2

li = []
di = {}

for _ in range(int(input())):
    li.append(input().strip())

for i in sorted(li):
    di[i] = len(i)
print(*sorted(di.keys(),key = lambda x:di[x]),sep='\n')

# 11286 절댓값 힙 https://www.acmicpc.net/problem/11286

import heapq as hq
h = []

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if not h:print(0)
        else:
            a = hq.heappop(h)
            print(a[1])
    else:
        hq.heappush(h,(-n,n)) if n < 0 else hq.heappush(h,(n,n))
