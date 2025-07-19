def solution(participant, completion):
    chk = {}
    for p in participant:
        if p in chk:
            chk[p] += 1
        else:
            chk[p] = 1
    for c in completion:
        chk[c] -= 1
        if chk[c] == 0:
            del chk[c]
    
    for i in chk:
        answer = i
    return answer