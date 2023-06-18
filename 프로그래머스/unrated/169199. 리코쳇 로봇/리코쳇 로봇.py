def solution(board):
    # 격자 가로, 세로
    m, n = len(board), len(board[0])
    # 큐
    q = []
    # visited
    visited = [[0 for _ in range(n)] for _ in range(m) ]
    # 상하좌우
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 로봇 위치 찾아 큐에 추가
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'R':
                q.append([i, j])
                visited[i][j] = 1

    # bfs
    while q:
        i, j = q.pop(0)
        if board[i][j] == 'G':
            return visited[i][j] - 1
        # 4방향 회전
        for di, dj in d:
            a, b = i, j
            # 격자 내에 있고 이동 후 값이 D가 아닌 경우
            while 0 <= (a+di) < m and 0 <= (b+dj) < n and board[a+di][b+dj] != 'D':
                a, b = a+di, b+dj
            else:
                if visited[a][b] == 0:
                    q.append([a, b])
                    visited[a][b] = visited[i][j] + 1
    return -1