def solution(arr):
    answer = []
    t = -1
    for a in arr:
        if a != t:
            t = a
            answer.append(a)
    return answer