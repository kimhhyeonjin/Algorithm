def dfs(x, y):
    if x == r-1 and y == c-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    cnt = 0
    for i in range(4):
        if 0 <= x + d[i][0] < r and 0 <= y + d[i][1] < c and road[x][y] > road[x+d[i][0]][y+d[i][1]]:
            cnt += dfs(x+d[i][0], y+d[i][1])
    visited[x][y] = cnt
    return visited[x][y]

r, c = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(r)]
visited = [[-1] * c for _ in range(r)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우
print(dfs(0, 0))