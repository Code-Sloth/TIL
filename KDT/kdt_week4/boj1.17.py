# 9085 더하기

for _ in range(int(input())):
    total = 0
    n = int(input())
    nums = list(map(int,input().split()))
    print(sum(nums))

# 10824 네 수

a,b,c,d = input().split()
print(int(a+b)+int(c+d))

# 3009 네 번째 점

aa,bb = [0]*3,[0]*3
for i in range(3):
    a,b = map(int,input().split())
    aa[i] = a
    bb[i] = b

for aaa in aa:
    if aa.count(aaa) == 1:
        print(aaa,end=' ')
for bbb in bb:
    if bb.count(bbb) == 1:
        print(bbb)

# 10952 A+B - 5

while 1:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    print(a+b)

# 1110 더하기 사이클

# sol 1 int

t = 0
n = int(input())
n_end = n

while 1:
    n2 = n//10 + n%10
    n = n%10*10 + n2%10
    t += 1
    if n == n_end:
        print(t)
        break

# sol 2 str

t = 0
n = int(input())
n_end = n

while 1:
    n2 = n//10 + n%10
    n = int(str(n%10) + str(n2%10))
    t += 1
    if n == n_end:
        print(t)
        break