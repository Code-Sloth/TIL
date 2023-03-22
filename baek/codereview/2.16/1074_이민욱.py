# 1074 Z

n,r,c = map(int,input().split())
t = 0

def z(n,i,j):
    global t
    nn = n//2
    if n == 2:
        for ii in range(2):
            for jj in range(2):
                t += 1
                if i+ii == r and j+jj == c:
                    print(t-1)
                    exit()
        return
    if not (i <= r < i + n and j <= c < j + n):
        t += n**2
        return
    
    z(nn,i,j)
    z(nn,i,j+nn)
    z(nn,i+nn,j)
    z(nn,i+nn,j+nn)

z(2**n,0,0)