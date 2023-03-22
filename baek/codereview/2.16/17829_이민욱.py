# 17829 222-풀링

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]

def divide(n,arr):
    nn = n//2
    if n == 1:
        return arr[0][0]
    li = [[0]* nn for _ in range(nn)]
    for i in range(0,n,2):
        for j in range(0,n,2):
            mx = []
            for i2 in range(2):
                for j2 in range(2):
                    mx.append(arr[i+i2][j+j2])
            li[i//2][j//2] = sorted(mx)[2]
    return divide(nn,li)

print(divide(n,g))