def solution(priorities, location):
    answer = 1
    loc = 0
    while sum(priorities):
        M = max(priorities)
        loc = loc % len(priorities)
        if priorities[loc] == M:
            priorities[loc] = 0
            if location == loc:
                break
            else:
                answer += 1
        loc += 1
    return answer