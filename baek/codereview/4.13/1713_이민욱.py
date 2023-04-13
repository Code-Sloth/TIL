# 1713 후보 추천하기
# 31256KB / 40ms

n = int(input())
m = int(input())
g = list(map(int,input().split()))

po = []
pi = []

for i in g: # 추천받은 번호 한 개씩 확인
    if i not in pi: # 해당 번호가 사진틀에 없으면
        if len(pi) >= n: # 사진틀이 꽉 찼으면
            pi.pop(po.index(min(po))) # 사진틀에서 최소중의 맨 앞의 번호를 뺌
            po.pop(po.index(min(po))) # 똑같이 추천 횟수도 뺌
        pi.append(i) # 사진틀이 꽉 차든 안 차든 오른쪽 끝에 추가
        po.append(1) # 처음 들어가는 거니 추천수 1로 추가
    else: # 해당 번호가 사진틀에 있으면
        po[pi.index(i)] += 1 # 해당 번호의 추천수를 1 증가

print(' '.join(map(str,sorted(pi)))) # 사전순 정렬되게 출력