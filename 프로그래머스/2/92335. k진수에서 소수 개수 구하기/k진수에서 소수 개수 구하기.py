def solution(n, k):
    answer = 0
    
    base_num = ''
    while n:
        base_num = str(n % k) + base_num
        n //= k
    base_list = list(map(str, base_num.split('0')))
    
    for b in base_list:
        if b == '':
            continue
        b = int(b)
        if b == 1:
            continue
        for i in range(2, int(b ** 0.5) + 1):
            if b % i == 0:
                break
        else:
            answer += 1

    return answer