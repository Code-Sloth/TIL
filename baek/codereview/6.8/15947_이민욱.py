# 15947 아기 석환 뚜루루 뚜루
# 31256KB/40ms

import sys
input = sys.stdin.readline

g = ['.', 'baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu', 'in', 'bed', 'tururu', 'turu', 'baby', 'sukhwan']

n = int(input())
n_re = n % 14       # 나머지
n_sh = n // 14      # 몫

if not n_re: n_re = 14  # 나머지가 0이면 sukhwan을 못 뽑으니 14로 만듦

if 'turu' in g[n_re]:                       # 해당 인덱스 문자열에 turu가 있으면
    result = g[n_re] + 'ru'*n_sh            # 반복횟수만큼 ru를 곱해서 더해줌
    if 'rururururu' in result:              # ru가 5번 이상 반복되면
        print(f"tu+ru*{result.count('r')}")
    else:
        print(result)
else:                                       # ru 없으면 그냥 출력
    print(g[n_re])