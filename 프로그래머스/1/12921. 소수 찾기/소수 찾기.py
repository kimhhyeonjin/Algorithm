def solution(n):
    answer = 0
    num = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if num[i]:
            answer += 1
            for j in range(i, n + 1, i):
                num[j] = 0
    return answer