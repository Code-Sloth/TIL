# 2108 통계학

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

from collections import Counter

def func3(li):
    mode_li = Counter(li).most_common(2)

    if len(mode_li) > 1 and mode_li[0][1] == mode_li[1][1]:
        return mode_li[1][0]
    return mode_li[0][0]

def func1(li):
     return round(sum(li)/len(li))

def func2(li):
     return li[len(li)//2]

def func4(li):
     return max(li)-min(li)

li = [int(input()) for x in range(int(input()))]
li.sort()

print(func1(li),func2(li),func3(li),func4(li),sep='\n')