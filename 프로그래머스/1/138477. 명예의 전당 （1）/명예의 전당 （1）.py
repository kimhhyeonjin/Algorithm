def solution(k, score):
    answer = []
    temp = []
    for s in score:
        if len(temp) < k:
            temp.append(s)
        else:
            if temp[-1] < s:
                temp[-1] = s
        temp.sort(reverse = True)
        answer.append(temp[-1])
    return answer