# 4889 안정적인 문자열
# 31256KB / 48ms

import sys
input = sys.stdin.readline

i = 0
while 1:
    i += 1
    s = input().rstrip()
    if '-' in s: break

    scount, t = 0, 0
    for st in s:
        if st == '{':           # { 만나면 + 1
            scount += 1
        else:
            if scount:          # } 인데 이미 들어있으면 - 1
                scount -= 1
            else:               # } 인데 비어있으면 안정적이지 않아 + 1
                t += 1
                scount += 1
    print(f'{i}. {t + scount//2}')