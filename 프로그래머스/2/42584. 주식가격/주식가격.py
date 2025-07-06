def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    for i in range(1, len(prices)):
        if i == len(prices) - 1:
            while stack:
                temp = stack.pop()
                answer[temp] = i - temp
        while stack and prices[stack[-1]] > prices[i]:
            temp = stack.pop()
            answer[temp] = i - temp
        stack.append(i)
    return answer