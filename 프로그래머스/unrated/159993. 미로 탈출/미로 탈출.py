from collections import deque

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def solution(maps):
    def bfs(start, end, visited):
        q = deque()
        q.append(start)
        visited[start[0]][start[1]] = 1
        while q:
            a, b = q.popleft()
            if a == end[0] and b == end[1]:
                return visited[a][b] - 1
            for di, dj in d:
                if 0 <= a+di < N and 0 <= b+dj < M and maps[a+di][b+dj] != "X":
                    if visited[a+di][b+dj] == 0:
                        visited[a+di][b+dj] = visited[a][b] + 1
                        q.append([a+di, b+dj])
        return -1
    N = len(maps)
    M = len(maps[0])
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                start = [i, j]
            if maps[i][j] == 'L':
                lever = [i, j]
            if maps[i][j] == 'E':
                end = [i, j]
    
    # lever bfs
    visited_l = [[0] * M for _ in range(N)]
    l = bfs(start, lever, visited_l)
    
    # end bfs
    if l == -1:
        answer = -1
    else:
        visited_e = [[0] * M for _ in range(N)]
        e = bfs(lever, end, visited_e)
        if e == -1:
            answer = -1
        else:
            answer = l + e
    return answer