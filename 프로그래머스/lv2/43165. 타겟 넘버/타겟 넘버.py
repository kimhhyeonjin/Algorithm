def solution(numbers, target):
    answer = 0
    visited = [0] * len(numbers)
    def dfs(i, val):
        # global과 nonlocal
        # global은 일반 함수 내에서 전역 변수를 대상으로 함
        # nonlocal은 중첩 함수 내에서 비지역 변수를 대상으로 함
        # 아래의 경우 nonlocal이 아닌 global answer으로 하면
        # NameError 발생
        nonlocal answer
        if i == len(numbers):
            if val == target:
                answer += 1
            return
        if visited[i] == 0:
            visited[i] += 1
            dfs(i+1, val + numbers[i])
        if visited[i] == 1:
            visited[i] -= 1
            dfs(i+1, val - numbers[i])
    dfs(0, 0)
    return answer