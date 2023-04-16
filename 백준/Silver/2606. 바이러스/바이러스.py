def dfs(v):
    global cnt
    visited[v] = 1

    for w in adjList[v]:
        if visited[w] == 0:
            dfs(w)
            cnt += 1

T = int(input())
E = int(input())
visited = [0] * (T + 1)
adjList = [[] for _ in range(T+1)]
for i in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

cnt = 0
dfs(1)
print(cnt)