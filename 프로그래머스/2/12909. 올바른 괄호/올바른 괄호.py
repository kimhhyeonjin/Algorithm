def solution(s):
    answer = False
    
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            if len(stack):
                stack.pop()
            else:
                break
    else:
        if len(stack) == 0:
            answer = True

    return answer