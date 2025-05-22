def solution(s):
    # 방법1
    answer = 0
    for i in range(len(s)):
        if s[i] != "+" and s[i] != "-":
            answer *= 10
            answer += int(s[i])
    if s[0] == "-":
        answer *= -1
    
    # 방법2
    # answer = int(s)
    
    return answer