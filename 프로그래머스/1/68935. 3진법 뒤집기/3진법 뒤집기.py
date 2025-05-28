def solution(n):
    answer = 0
    
    new_n = ""
    while n != 0:
        new_n = str(n % 3) + new_n
        n = n // 3
    
    t = 1
    for i in range(len(new_n)):
        answer += int(new_n[i]) * t
        t *= 3
    
    return answer