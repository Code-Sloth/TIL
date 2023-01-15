import sys
sys.stdin = open('input.txt','r')

for i in range(int(input())):
    s = list(input().split())
    print(s)
    num = int(s.pop(0))
    print(s)
    print(num)
    for alpha in str(s[0]):
        print(alpha*num,end='')
    print()