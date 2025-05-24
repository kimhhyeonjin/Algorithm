def solution(num):
    answer = 0
    t = 0
    while t < 500:
        if num == 1:
            answer = t
            break
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        t += 1
    if num != 1:
        answer = -1
    return answer