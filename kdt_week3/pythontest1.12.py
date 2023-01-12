# 2072 홀수만 더하기

for i in range(1,int(input())+1):
    nums = list(map(int,input().split()))
    sum = 0
    for n in nums:
        if n % 2 == 1:
            sum += n
    print(f'#{i} {sum}')

# 2056 연월일 달력

li=[]
for k in range(1,13):
    if k == 2:
        li.append(range(1,29))
    elif k==4 or k==6 or k==9 or k==11:
        li.append(range(1,31))
    else:
        li.append(range(1,32))
    

for i in range(1,int(input())+1):
    n = input()
    if int(n[4:6]) == 0 or int(n[4:6]) > 12:
        print(f'#{i} -1')
    else:
        if int(n[6:8]) in li[int(n[4:6])-1]:
            print(f'#{i} {n[:4]}/{n[4:6]}/{n[6:8]}')
        else:
            print(f'#{i} -1')

# 2043 서랍의 비밀번호

p, k = map(int,input().split())
print(p-k+1)

# 1933 간단한 N의 약수

n = int(input())

for i in range(1,n+1):
    if n % i == 0:
        print(i,end=' ')

# 1288 새로운 불면증 치료법

t = int(input())

for i in range(1,t+1):
    di = {}
    n = input() # 1259
    k = 0
    while 1:
        k += 1 # 1 2 3 4 5 6
        n2 = int(n)*k # 1259*1 1259*2 1259*3
        for j in str(n2): # '1' '2' '5' '9' '2' '5' '1' '8'
            di[int(j)] = 1
            num = n2
        if len(di) > 9:
            break
    print(f'#{i} {num}')