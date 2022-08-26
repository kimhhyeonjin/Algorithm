N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
max_rng = 0
for num in range(1, N+1):
    i, j, x, y = map(int, input().split())
    max_rng = max(max_rng, i+x, y+j)
    for r in range(x):
        for c in range(y):
            arr[i+r][j+c] = num

# print(arr)

for num in range(1, N+1):
    cnt = 0
    for row in range(max_rng):
        for col in range(max_rng):
            if arr[row][col] == num:
                cnt += 1
    print(cnt)