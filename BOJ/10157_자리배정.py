C, R = map(int, input().split())
K = int(input())

arr = []
for _ in range(R):
    arr.append(list([0] * C))
print(arr)

M = [[0, -1], [1, 0], [0, 1], [-1, 0]]
i, j, k = 0, R-1, 0
num = 0

