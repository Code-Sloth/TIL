# 4659 비밀번호 발음하기
# 31256KB / 52ms

g = ['a','e','i','o','u']

while 1:
    s = input().rstrip()
    if s == 'end': break
    is_bc = 0
    is_ai = 0
    is_1 = False
    is_2 = True
    is_3 = True
    for i in range(len(s)):
        if s[i] in g:
            is_1 = True
            is_ai += 1
            is_bc = 0
        else:
            is_ai = 0
            is_bc += 1
        if is_bc >= 3 or is_ai >= 3:
            is_2 = False
        if i > 0:
            if s[i] == s[i-1]:
                if s[i] != 'e' and s[i] != 'o':
                    is_3 = False
                    break
    if is_1 and is_2 and is_3:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')