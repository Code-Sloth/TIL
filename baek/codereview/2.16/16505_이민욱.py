# 16505 별

n = int(input())
g = [[' ']*(2**n) for _ in range(2**n)]

def star(n,i,j):
    if n == 0:
        g[i][j] = '*'
        return
    if n == 1:
        g[i][j],g[i][j+1],g[i+1][j] = '*','*','*'
        return

    nn = 2**n//2
    star(n-1,i,j)
    star(n-1,i+nn,j)
    star(n-1,i,j+nn)

star(n,0,0)
for i in g:
    print(''.join(i).rstrip())