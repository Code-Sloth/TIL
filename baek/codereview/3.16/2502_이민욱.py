# 2502 떡 먹는 호랑이
# 31256KB / 112ms

d, k = map(int,input().split())

fibo = [0] * (d+1)
fibo[1] = fibo[2] = 1

while fibo[d] != k:
    for i in range(3,d+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    
    if fibo[d] < k:
        fibo[2] += 1
    elif fibo[d] > k:
        fibo[1] += 1
        fibo[2] = fibo[1]

print(fibo[1],fibo[2],sep = '\n')