def solution(s):
    answer = ''
    
    space = 1
    for i in s:
        if i == ' ':
            answer += ' '
            space = 1
        else:
            if space:
                answer += i.upper()
            else:
                answer += i.lower()
            space = (space + 1) % 2
        
    return answer 