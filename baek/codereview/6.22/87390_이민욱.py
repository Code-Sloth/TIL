# 프로그래머스 87390 n^2 배열 자르기

def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n, i%n)+1)
    
    return answer

# 처음 풀이
# 시간초과

# def solution(n, left, right):
#     answer = []
#     cnt = -1
    
#     for i in range(n):
#         for j in range(n):
#             cnt += 1
#             if left <= cnt <= right:
#                 answer.append(max(i+1,j+1))
#             if cnt > right: break
            
#     return answer