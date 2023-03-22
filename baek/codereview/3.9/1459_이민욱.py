# 1459 걷기
# 31256KB / 44ms

x,y,a,b = map(int,input().split())
mx,mn = max(x,y),min(x,y)
result = []

if (x+y) % 2 == 0: # 대각
    result.append(mx*b)
else: # 대각 / 평행1
    result.append((mx-1) * b + a)
    
result.append((x+y) * a) # 평행
result.append((mn*b)+(mx-mn)*a) # 대각 / 평행

print(min(result))