def solution(priorities, location):
    answer = 0
    i = 0
    max_p = max(priorities)
    
    while True:
        if priorities[i] == max_p:
            answer += 1
            priorities[i] = 0
            max_p = max(priorities)
            if i == location:
                break
        i = (i + 1) % len(priorities)
    return answer