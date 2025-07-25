def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    
    cam = -30001
    for r in routes:
        if cam < r[0]:
            cam = r[1]
            answer += 1
    return answer