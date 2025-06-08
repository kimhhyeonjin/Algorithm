def solution(clothes):
    answer = 1
    c = {}
    
    for i in clothes:
        if i[1] in c:
            c[i[1]] += 1
        else:
            c[i[1]] = 1
    
    for j in c:
        answer *= (c[j] + 1)
    answer -= 1
    
    return answer