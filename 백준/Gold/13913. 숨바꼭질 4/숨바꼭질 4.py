from collections import deque

def path(i):
    arr = []
    temp = i
    for _ in range(road[i]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs(idx):
    q = deque()
    q.append(idx)
    road[idx] = 0
    while q:
        i = q.popleft()
        if i == K:
            print(road[i])
            path(i)
            return
        for nxt in [i+1, i-1, 2*i]:
            if 0 <= nxt < 100001 and road[nxt] == -1:
                q.append(nxt)
                road[nxt] = road[i] + 1
                move[nxt] = i

N, K = map(int, input().split())
road = [-1] * 100001
move = [-1] * 100001
bfs(N)