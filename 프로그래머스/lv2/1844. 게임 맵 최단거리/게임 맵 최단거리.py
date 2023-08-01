from collections import deque

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]
    
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    
    # bfs
    while q:
        a, b = q.popleft()
        # print(a, b)
        if a == N-1 and b == M-1:
            return visited[a][b]
        for di, dj in d:
            if 0 <= a+di < N and 0 <= b+dj < M and maps[a+di][b+dj] == 1:
                if visited[a+di][b+dj] == 0:
                    visited[a+di][b+dj] = visited[a][b] + 1
                    q.append([a+di, b+dj])
    return -1