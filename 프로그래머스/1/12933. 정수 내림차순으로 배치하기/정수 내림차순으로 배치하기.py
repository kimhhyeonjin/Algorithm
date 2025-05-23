def solution(n):
    new_n = list(str(n))
    
    # 방법1
    for i in range(len(new_n)-1, -1, -1):
        for j in range(i):
            if new_n[j] < new_n[j+1]:
                new_n[j], new_n[j+1] = new_n[j+1], new_n[j]
    
    # 방법2
    # new_n.sort(reverse = True)
    
    answer = int("".join(new_n))
    
    return answer