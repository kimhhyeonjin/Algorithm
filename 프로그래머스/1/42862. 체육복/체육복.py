def solution(n, lost, reserve):
    stu = [1] * n
    
    for l in lost:
        stu[l-1] = 0
        
    reserve.sort()
    for r in reserve:
        if r in lost:
            stu[r-1] = 1
        elif 0 <= r - 2 and stu[r-2] == 0:
            stu[r-2] = 1
        elif r < n and stu[r] == 0:
            stu[r] = 1
    
    answer = sum(stu)
    return answer