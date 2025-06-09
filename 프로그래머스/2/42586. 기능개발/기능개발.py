def solution(progresses, speeds):
    answer = []
    
    while progresses and progresses[0] < 100:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            cnt = 0
            for j in range(len(progresses)):
                if progresses[j] >= 100:
                    cnt += 1
                else:
                    progresses = progresses[j:]
                    speeds = speeds[j:]
                    answer.append(cnt)
                    break
            else:
                answer.append(cnt)
                progresses = []
    return answer