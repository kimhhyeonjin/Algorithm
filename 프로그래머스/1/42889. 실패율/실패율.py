def solution(N, stages):
    answer = []
    cnt = []
    
    for i in range(1, N+1):
        if len(stages):
            cnt.append([i, stages.count(i) / len(stages)])
            stages = [x for x in stages if x != i]
            # 아래로 하면 시간초과
            # while i in stages:
            #     stages.remove(i)
        else:
            cnt.append([i, 0])
        
    cnt.sort(reverse = True, key = lambda x : x[1])
    for i, j in cnt:
        answer.append(i)
    
    return answer