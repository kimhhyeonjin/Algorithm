def solution(n, computers):
    visited = [0] * n


    def dfs(i):
        for w in range(n):
            if w != i and computers[i][w] == 1 and visited[w] == 0:
                visited[w] = 1
                dfs(w)


    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            cnt += 1
            dfs(i)

    return cnt