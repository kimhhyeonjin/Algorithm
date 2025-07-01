def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < numbers[idx]:
            i = stack.pop()
            answer[i] = num
        stack.append(idx)
    
    return answer