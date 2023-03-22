# 11497 통나무 건너뛰기
# 32276KB / 172ms

# 최댓값을 센터로 두고 양 옆으로 하나씩 배치
for _ in range(int(input())):
    n = int(input())
    g = sorted(list(map(int,input().split())),reverse=True)
    mx = g[0] - g[1]
    for i in range(n-2):
        if mx < g[i] - g[i+2]:
            mx = g[i] - g[i+2]

    print(mx)


# 처음 풀이

# from collections import deque

# for _ in range(int(input())):
#     n = int(input())
#     g = sorted(list(map(int,input().split())))
#     mx = 0
#     result = deque([g[-1]])

#     while g:
#         result.append(g.pop())
#         if abs(result[-1] - result[-2]) > mx:
#             mx = abs(result[-1] - result[-2])

#         if g:
#             result.appendleft(g.pop())
#             if abs(result[0] - result[1]) > mx:
#                 mx = abs(result[0] - result[1])
    
#     print(mx)