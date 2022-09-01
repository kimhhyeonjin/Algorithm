import sys
sys.stdin = open('txt.txt')

C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print(0)
else:
    arr = []
    for _ in range(R):
        arr.append(list([0] * C))
    # print(arr)

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    i, j, k = R-1, 0, 0
    num = 1

    arr[i][j] = num
    while num < C*R:
        i, j = i+di[k], j+dj[k]
        if 0 <= i < C and 0 <= j < R and arr[i][j] == 0:
            num += 1
            arr[i][j] = num
        else:
            i, j = i - di[k], j - dj[k]
            k = (k+1) % 4
            i, j = i + di[k], j + dj[k]
            num += 1
            arr[i][j] = num
    print(i, j)

