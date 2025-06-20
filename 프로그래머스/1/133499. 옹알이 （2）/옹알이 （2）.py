def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    for p in pron:
        for i in range(len(babbling)):
            if p*2 not in babbling[i]:
                if p in babbling[i]:
                    babbling[i] = babbling[i].replace(p, ' ')
    
    for b in babbling:
        if len(b.strip()) == 0:
            answer += 1
    
    return answer