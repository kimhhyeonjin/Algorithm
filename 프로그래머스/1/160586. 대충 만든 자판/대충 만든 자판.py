def solution(keymap, targets):
    answer = []
    k = {}
    
    for i in keymap:
        for j in range(len(i)):
            if i[j] not in k:
                k[i[j]] = j + 1
            else:
                k[i[j]] = min(k[i[j]], j + 1)
    
    for tar in targets:
        temp = 0
        for t in tar:
            if t not in k:
                answer.append(-1)
                break
            temp += k[t]
        else:
            answer.append(temp)
    return answer