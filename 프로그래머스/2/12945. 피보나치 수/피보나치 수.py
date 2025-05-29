def solution(n):    
    n_list = [0, 1]
    for _ in range(n-1):
        n_list.append(n_list[-1] + n_list[-2])
    
    answer = n_list[-1] % 1234567
    return answer