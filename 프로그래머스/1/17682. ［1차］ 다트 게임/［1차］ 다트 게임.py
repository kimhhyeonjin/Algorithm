def solution(dartResult):
    answer = 0
    result = [0] * 3
    
    i = -1
    n = ''
    for d in range(len(dartResult)):
        if dartResult[d].isdigit():
            if not dartResult[d + 1].isdigit():
                i += 1
            n += dartResult[d]
        else:
            if n:
                num = int(n)
            n = ''
            if dartResult[d] == 'S':
                result[i] += num
            if dartResult[d] == 'D':
                result[i] += num ** 2
            if dartResult[d] == 'T':
                result[i] += num ** 3
            if dartResult[d] == '*':
                result[i] *= 2
                if i != 0:
                    result[i - 1] *= 2
            if dartResult[d] == '#':
                result[i] *= -1
        answer = sum(result)
    return answer