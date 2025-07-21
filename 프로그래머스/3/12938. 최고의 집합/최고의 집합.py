def solution(n, s):
    answer = []
    if s < n:
        answer.append(-1)
    else:
        m = s % n
        for i in range(n - m):
            answer.append(s // n)
        for i in range(m):
            answer.append(s // n + 1)
    return answer