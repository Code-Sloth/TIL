import sys
sys.stdin = open('input.txt','r')

s = input()
t = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        t+=1

print((t+1)//2)

# import sys
# sys.stdin = open('input.txt','r')

# s = input()

# li1 = []
# li2 = []

# for i in range(len(s)-1):
#     if s[i] != s[i+1]:
#         li1.append(s[i+1])
#         li2.append(i+1)

# if len(li1) > 1:
#     print(len(li2[::2]))
# elif len(li1) == 1:
#     print(1)
# else:
#     print(0)