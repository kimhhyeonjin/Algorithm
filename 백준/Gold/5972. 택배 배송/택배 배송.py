from heapq import heappush, heappop

def dijkstra(start):
    h = []
    d[start] = 0
    heappush(h, (0, start))
    while h:
        dist_u, u = heappop(h)
        if d[u] < dist_u:
            continue
        for v, w in road[u]:
            dist_v = dist_u + w
            if dist_v < d[v]:
                d[v] = dist_v
                heappush(h, (dist_v, v))

N, M = map(int, input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    road[a].append([b, c])
    road[b].append([a, c])

d = [1e9] * (N+1)
dijkstra(1)
print(d[N])