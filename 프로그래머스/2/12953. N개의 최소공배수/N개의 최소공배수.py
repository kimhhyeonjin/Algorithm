def solution(arr):
    max_V = max(arr)
    for i in range(max_V, max_V ** 15):
        for a in arr:
            if i % a != 0:
                break
        else:
            answer = i
            break
    return answer