N, M, V = map(int, input().split())
adjList = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)
# print(adjList)
# 방문할 수 있는 점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문
for i in range(1, N+1):
    adjList[i].sort()
# print(adjList)
d = []
d_visited = [0 for _ in range(N+1)]
b = []
b_visited = [0 for _ in range(N+1)]

def dfs(v):
    d_visited[v] = 1
    d.append(v)
    for w in adjList[v]:
        if d_visited[w] == 0:
            d_visited[w] = 1
            dfs(w)

def bfs(v):
    bq = []
    bq.append(v)
    b_visited[v] = 1
    while bq:
        v = bq.pop(0)
        b.append(v)
        for w in adjList[v]:
            if b_visited[w] == 0:
                b_visited[w] = 1
                bq.append(w)

dfs(V)
# print(d)
print(*d)
bfs(V)
# print(b)
print(*b)