def solution(order):
    answer = 0
    stack = []
    
    o = 0
    i = 1
    while i <= len(order) or o < len(order):
        if i < order[o]:
            stack.append(i)
            i += 1
        elif i == order[o]:
            answer += 1
            i += 1
            o += 1
        else:
            temp = stack.pop()
            if temp == order[o]:
                answer += 1
                o += 1
            else:
                break
    return answer