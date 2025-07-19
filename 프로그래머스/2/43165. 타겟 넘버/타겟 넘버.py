answer = 0

def dfs(num, target, d, depth, numbers):
    global answer
    
    if d == depth:
        if num == target:
            answer += 1
        return
    else:
        dfs(num + numbers[d], target, d + 1, depth, numbers)
        dfs(num - numbers[d], target, d + 1, depth, numbers)

def solution(numbers, target):
    global answer
    dfs(0, target, 0, len(numbers), numbers)

    return answer