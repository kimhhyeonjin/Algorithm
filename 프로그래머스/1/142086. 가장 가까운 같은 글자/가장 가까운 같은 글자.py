def solution(s):
    answer = []
    d = dict()
    for i in range(len(s)):
        if s[i] in d:
            answer.append(i - d[s[i]])
        else:
            answer.append(-1)
        d[s[i]] = i
    return answer