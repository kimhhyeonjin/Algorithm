def solution(s):
    answer = 0
    
    while s:
        x = s[0]
        for i in range(len(s)):
            if len(s[:i+1]) == s[:i+1].count(x) * 2:
                answer += 1
                s = s[i+1:]
                break
        else:
            answer += 1
            break
    return answer