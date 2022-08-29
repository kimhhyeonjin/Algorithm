import sys
sys.stdin = open('1961_숫자배열회전.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(input().split()))

    d90 = []
    for i in range(N):
        text90 = ''
        for j in range(N-1, -1, -1):
            text90 += arr[j][i]
        d90.append(text90)
    # print(d90)

    d180 = []
    for i in range(N-1, -1, -1):
        text180 = ''
        for j in range(N-1, -1, -1):
            text180 += arr[i][j]
        d180.append(text180)
    # print(d180)

    d270 = []
    for i in range(N-1, -1, -1):
        text270 = ''
        for j in range(N):
            text270 += arr[j][i]
        d270.append(text270)
    # print(d270)

    print(f'#{tc}')
    for k in range(N):
        print(d90[k], d180[k], d270[k])