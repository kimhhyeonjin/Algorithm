def solution(a, b):
    answer = 0
    if a == b:
        answer = a
        return answer
    elif a > b:
        a, b = b, a
    for i in range(a, b + 1):
        answer += i
    return answer