import sys
sys.setrecursionlimit(10**9)

def dfs(idx, d):
    global answer
    if d == 5:
        answer = True
        return
    visited[idx] = 1
    for nxt in friends[idx]:
        if not visited[nxt]:
            dfs(nxt, d+1)
    visited[idx] = 0

N, M = map(int, input().split())
friends = [[] for _ in range(N)]
visited = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

answer = False
for i in range(N):
    dfs(i, 1)
    if answer:
        break

if answer:
    print(1)
else:
    print(0)