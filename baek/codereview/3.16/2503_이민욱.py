# 2503 숫자 야구
# 31256KB / 44ms

from itertools import permutations

n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
per = list(permutations([1,2,3,4,5,6,7,8,9],3))
t = 0

for a in per:
	cnt = 0
	for i in range(n):
		s = b = 0
		sn = list(map(int,str(li[i][0])))
		for j in range(3):
			if a[j] == sn[j]:
				s += 1
			else:
				if a[j] in sn:
					b += 1
		if s != li[i][1] or b != li[i][2]:
			cnt = 0
			break
		else:
			cnt += 1
	if cnt == n:
		t += 1
		
print(t)