def solution(d, budget):
    answer = 0
    
    d.sort()
    new_d = 0
    for i in range(len(d)):
        if new_d + d[i] <= budget:
            new_d += d[i]
            answer += 1
        else:
            break
    
    return answer