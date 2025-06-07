def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for c in range(len(citations) - 1 , -1, -1):
        if citations[c] >= c + 1:
            answer = c + 1
            break
    return answer