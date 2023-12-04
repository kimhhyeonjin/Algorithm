from collections import deque

def bfs(idx):
    q = deque()
    q.append(idx)
    road[idx] = 0
    while q:
        x = q.popleft()
        if x == K:
            return road[K]
        if 0 < x*2 < 100001 and road[x*2] == -1:
            road[x*2] = road[x]
            # 순간이동 우선순위를 제일 앞으로
            q.appendleft(x*2)
        if 0 <= x-1 < 100001 and road[x-1] == -1:
            road[x-1] = road[x] + 1
            q.append(x-1)
        if 0 <= x+1 < 100001 and road[x+1] == -1:
            road[x+1] = road[x] + 1
            q.append(x+1)

N, K = map(int, input().split())
road = [-1] * 100001
print(bfs(N))