arr = [[0 for _ in range(100)] for _ in range(100)]
# print(arr)

for _ in range(4):
    square = list(map(int, input().split()))
    for i in range(square[0], square[2]):
        for j in range(square[1], square[3]):
            arr[i][j] += 1

cnt = 0
for a in range(100):
    for b in range(100):
        if arr[a][b] > 0:
            cnt += 1
            
print(cnt)