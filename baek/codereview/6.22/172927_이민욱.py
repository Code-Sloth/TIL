# 프로그래머스 172927 광물 캐기

answer = int(1e9)
a = [[1,1,1], [5,1,1], [25,5,1]]
mineral = {
    'diamond': 0,
    'iron': 1,
    'stone': 2
}

def dfs(index, p, minerals, d, ir, s):
    if index >= len(minerals) or d + ir + s == 0: # 광물 다 캤거나 곡괭이 없을 때
        global answer
        answer = min(answer, p) # 피로도 최솟값 갱신
        return 

    dp, ip, sp = 0, 0, 0    # 재귀 한 번마다 더해줄 거니까 0으로 초기화
    for i in range(index, min(index+5, len(minerals))): # 광물 5개씩 반복
        dp += a[0][mineral[minerals[i]]]    # 해당하는 피로도만큼 더해줌
        ip += a[1][mineral[minerals[i]]]
        sp += a[2][mineral[minerals[i]]]

    if d:   # 다이아로 캘 때
        dfs(index+5, p+dp, minerals, d-1, ir, s)

    if ir:  # 철로 캘 때
        dfs(index+5, p+ip, minerals, d, ir-1, s)

    if sp:  # 돌로 캘 때
        dfs(index+5, p+sp, minerals, d, ir, s-1)
 
def solution(picks, minerals):
    global answer
    dfs(0, 0, minerals, picks[0], picks[1], picks[2]) # 완전탐색 DFS
    return answer