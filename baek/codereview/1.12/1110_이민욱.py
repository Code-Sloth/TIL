import sys
sys.stdin = open('input.txt','r')

# 2+6=8
# 6+8=14
# 8+4=12
# 4+2=6
n = int(input())
n2 = n # 26
cnt = 0

while True:
    end = n2//10 + n2%10      # 2 6 = 8   / 6 + 8 = 14
    n2 = (n2%10)*10 + end%10  # 60 8 = 68 / 80 + 4 = 84
    cnt += 1
    if n == n2:
        break
print(cnt)
