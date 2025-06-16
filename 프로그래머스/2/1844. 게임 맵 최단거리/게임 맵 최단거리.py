from collections import deque

def solution(maps):
    dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    d = deque()
    visited[0][0] = 1
    d.append([0, 0, 1])
    while d:
        i, j, k = d.popleft()
        if i == n - 1 and j == m - 1:
            return k
        for di, dj in dd:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                d.append([ni, nj, k + 1])
    
    return -1