# 16113 시그널
# 31388KB / 76ms

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
g = []
result = []
number = ['####.##.##.####',
          'x',
          '###..#####..###',
          '###..####..####',
          '#.##.####..#..#',
          '####..###..####',
          '####..####.####',
          '###..#..#..#..#',
          '####.#####.####',
          '####.####..####']

def num(index):
    num_s = ''
    for i in range(5):
        for j in range(3):
            num_s += g[i][index+j]
    for i in range(10):
        if num_s == number[i]:
            result.append(i)

def onefour(index):
    t = 0
    for i in range(5):
        if g[i][index+1] == '.' and g[i][index-1] == '.':
         t += 1
    if t == 5: result.append(1)
    else:
        num(index)

for i in range(0,n,n//5):
    g.append('..' + s[i:i+n//5] + '..')

for index in range(2,n//5+2):
    if g[0][index] == '#' and g[0][index+1] == '#' and g[0][index+2] == '#':
        num(index)
    elif g[0][index] == '#' and g[0][index+1] == '.' and g[0][index-1] == '.':
        onefour(index)

print(*result,sep='')

'''
185
###.#.###.###.#.#.###.###.###.###...#
#.#.#...#...#.#.#.#...#.....#.#.#...#
#.#.#.###.###.###.###.###...#.###...#
#.#.#.#.....#...#...#.#.#...#.#.#...#
###.#.###.###...#.###.###...#.###...#
'''