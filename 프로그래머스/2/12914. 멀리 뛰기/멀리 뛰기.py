def solution(n):
    jump = [1, 2] + [0] * n
    if n >= 3:
        for i in range(2, n):
            jump[i] = jump[i-1] + jump[i-2]
            
    answer = jump[n-1] % 1234567
    return answer