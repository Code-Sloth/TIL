# 프로그래머스 176962 과제 진행하기

def solution(plans):
    answer = []
    stop = []
    plan = sorted(plans, key=lambda x:x[1])

    for i in range(len(plan) - 1):
        # 현재 과목 시작 시간(분) - 다음 과목 시작 시간(분)
        time = (int(plan[i][1].split(':')[0]) - int(plan[i+1][1].split(':')[0]))*60 + (int(plan[i][1].split(':')[1]) - int(plan[i+1][1].split(':')[1]))
        # 현재 과목 진행한 시간만큼 빼줌 = 현재 과목 남은 시간
        remain_time = int(plan[i][2]) + time

        if remain_time > 0:   # 시간이 남아있으면
            stop.append([plan[i][0], remain_time])
        else:   # 다 들었으면
            answer.append(plan[i][0])
            while stop and remain_time < 0: # 멈춘 과목이 있고, 남은 시간이 음수일 때
                remain_time += stop[-1][1]  # 남은 시간에 멈춘 과목의 남은 시간을 더함
                if remain_time > 0:
                    stop[-1][1] = remain_time   # 남은 시간만큼 줬으니 갱신
                else:
                    answer.append(stop.pop()[0])    # 시간을 다 줬으면 답에 추가

    answer.append(plan[-1][0])  # 마지막 과목을 추가
    for s in stop[::-1]:        # 남은 멈춘 과목들을 순서대로 추가
        answer.append(s[0])

    return answer