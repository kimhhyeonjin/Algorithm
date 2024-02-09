def solution(elements):
    answer = set()
    elements_d = elements + elements
    for i in range(len(elements)):
        temp = 0
        for j in range(len(elements)):
            temp += elements_d[i+j]
            answer.add(temp)
            # print(temp)
    return len(answer)