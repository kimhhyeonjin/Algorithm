def solution(sizes):
    # print(sizes)
    for s in sizes:
        s.sort()
    # print(sizes)
    
    r, c = 0, 0
    for i, j in sizes:
        if r < i:
            r = i
        if c < j:
            c = j
    
    answer = r * c
    return answer