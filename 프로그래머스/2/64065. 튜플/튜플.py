def solution(s):
    answer = []
    
    list_s = []
    for i in range(1, len(s) - 1):
        if s[i] == '{':
            start = i
        elif s[i] == '}':
            end = i
            list_s.append(list(map(int, s[start + 1 : end].split(','))))
    list_s.sort(key = lambda x : len(x))
    
    for j in list_s:
        for k in j:
            if k not in answer:
                answer.append(k)
    return answer