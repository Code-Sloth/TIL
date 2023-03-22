import sys
sys.stdin = open('input.txt','r')

dish = input()
t = 10

for i in range(len(dish)-1):
    if dish[i] != dish[i+1]:
        t += 10
    else:
        t += 5
print(t)