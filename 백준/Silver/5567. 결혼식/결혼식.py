def bfs(v):
    global cnt
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        cnt += 1
        for w in adjList[v]:
            if visited[w] == 0:
                if visited[v] < 3:
                    visited[w] = visited[v] + 1
                    q.append(w)

N = int(input())
M = int(input())
visited = [0 for _ in range(N+1)]
adjList = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
cnt = 0
bfs(1)
# 상근이는 cnt에서 제외
print(cnt - 1)