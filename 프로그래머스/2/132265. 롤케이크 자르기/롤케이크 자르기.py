def solution(topping):
    answer = 0
    
    l = {}
    r = {}
    for t in topping:
        if t not in r:
            r[t] = 0
        r[t] += 1
    
    for i in topping:
        if i not in l:
            l[i] = 0
        l[i] += 1
        r[i] -= 1
        if r[i] == 0:
            r.pop(i)
        if len(l) == len(r):
            answer += 1
        
    return answer