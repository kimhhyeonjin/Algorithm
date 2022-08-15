T = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]
cnt = 0

for _ in range(T):
    i, j = map(int, input().split())
    for a in range(10):
        for b in range(10):
            arr[i+a][j+b] += 1
    
for m in range(100):
    for n in range(100):
        if arr[m][n] > 0:
            cnt += 1
    
print(cnt)