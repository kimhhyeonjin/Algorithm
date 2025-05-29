def solution(n):
    answer = 0
    cnt_n = str(bin(n)[2:]).count("1")
    
    for num in range(n+1, 10 ** 100):
        if str(bin(num))[2:].count("1") == cnt_n:
            answer = num
            break
    return answer