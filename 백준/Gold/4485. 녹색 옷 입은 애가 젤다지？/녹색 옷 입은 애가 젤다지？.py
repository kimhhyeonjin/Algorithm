from heapq import heappush, heappop

def dijkstra():
    h = []
    # h에 값과 좌표 추가
    heappush(h, (cave[0][0], [0, 0]))
    # 시작점의 값 입력
    d[0][0] = cave[0][0]
    while h:
        v, [x, y] = heappop(h)
        # 이미 최소값이면 continue
        if d[x][y] < v:
            continue
        # 아닌 경우 상하좌우 돌면서 최소값 갱신 여부 확인하고 갱신 및 h에 추가
        for di, dj in dd:
            if 0 <= x + di < n and 0 <= y + dj < n:
                u = v + cave[x+di][y+dj]
                if d[x+di][y+dj] > u:
                    d[x+di][y+dj] = u
                    heappush(h, (u, [x+di, y+dj]))

dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]
t = 1
while True:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    # 다익스트라
    d = [[1e9] * n for _ in range(n)]
    dijkstra()
    print(f'Problem {t}: {d[n-1][n-1]}')
    # print(d)
    t += 1