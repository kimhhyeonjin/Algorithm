def solution(number, limit, power):
    answer = 0
    
    for c in range(1, number + 1):
        temp = 0
        for i in range(1, int(c ** 0.5) + 1):
            if c % i == 0:
                temp += 1
                if i ** 2 != c:
                    temp += 1
        if temp > limit:
            temp = power
        answer += temp

    return answer

