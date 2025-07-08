def solution(land):
    for l in range(1, len(land)):
        for i in range(4):
            temp = 0
            for j in range(4):
                if i != j and temp < land[l-1][j] + land[l][i]:
                    temp = land[l-1][j] + land[l][i]
            land[l][i] = temp
    answer = max(land[-1])
    
    return answer