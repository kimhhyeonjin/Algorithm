def solution(x, n):
    answer = []
    sum_x = x
    for _ in range(n):
        answer.append(sum_x)
        sum_x += x
    return answer