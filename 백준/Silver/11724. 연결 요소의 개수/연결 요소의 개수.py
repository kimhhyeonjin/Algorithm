N, M = map(int, input().split())
adjList = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    # print(u, v)
    adjList[u].append(v)
    adjList[v].append(u)

def dfs(v):
    if visited[v] == 1:
        return
    if visited[v] == 0:
        visited[v] = 1
        for w in adjList[v]:
            if visited[w] == 0:
                dfs(w)

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        # 연결요소가 없는 경우 따로 세주기
        if not adjList[i]:
            pass
        else:
            dfs(i)
        cnt += 1
    else:
        continue
print(cnt)