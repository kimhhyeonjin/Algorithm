def solution(s):
    answer = ''
    t = True
    for ss in s:
        if ss == " ":
            answer += " "
            t = True
        elif type(ss) == int:
            answer += ss
            t = False
        else:
            if t:
                answer += ss.upper()
            else:
                answer += ss.lower()
            t = False
    return answer