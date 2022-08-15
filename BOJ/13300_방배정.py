N, K = map(int, input().split())

room = [[0 for _ in range(6)] for _ in range(2)]
# print(room)

for i in range(N):
    S, Y = map(int, input().split())
    room[S][Y-1] += 1
# print(room)

cnt = 0
for s in range(2):
    for y in range(6):
        if room[s][y] > 0:
            if room[s][y] % K == 0:
                cnt += room[s][y] // K
            else:
                cnt += room[s][y] // K + 1

print(cnt)