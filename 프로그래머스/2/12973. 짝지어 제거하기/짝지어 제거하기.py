def solution(s):
    new_s = list()
    
    for i in s:
        if len(new_s) == 0:
            new_s.append(i)
        elif new_s[-1] == i:
            new_s.pop()
        else:
            new_s.append(i)
    
    if new_s:
        answer = 0
    else:
        answer = 1

    return answer