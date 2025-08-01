def solution(numbers):
    numbers.sort(reverse = True, key = lambda x : str(x) * 4)
    
    answer = ''
    for n in numbers:
        answer += str(n)
    if len(answer) == answer.count('0'):
        answer = '0'
    return answer