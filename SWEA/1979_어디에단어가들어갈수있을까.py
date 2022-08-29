import sys
sys.stdin = open('1979_어디에단어가들어갈수있을까.txt')

T = int(input())

for tc in range(1, T+1):

    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    t_cnt = 0

    # 가로
    for i in range(N):
        for j in range(N-K+1):
            r_cnt = 0
            for k in range(K):
                if arr[i][j+k] == 1:
                    r_cnt += 1
            if r_cnt == K:
                if N == K:
                    t_cnt += 1
                elif j+k == N-1:
                    if arr[i][j+k-K] == 0:
                        t_cnt += 1
                elif j == 0:
                    if arr[i][j+k+1] == 0:
                        t_cnt += 1
                elif arr[i][j+k-K] == 0 and arr[i][j+k+1] == 0:
                    t_cnt += 1

    # 세로 (전치행렬 이용)
    c_arr = list(zip(*arr))
    for i in range(N):
        for j in range(N-K+1):
            r_cnt = 0
            for k in range(K):
                if c_arr[i][j+k] == 1:
                    r_cnt += 1
            if r_cnt == K:
                if N == K:
                    t_cnt += 1
                elif j+k == N-1:
                    if c_arr[i][j+k-K] == 0:
                        t_cnt += 1
                elif j == 0:
                    if c_arr[i][j+k+1] == 0:
                        t_cnt += 1
                elif c_arr[i][j+k-K] == 0 and c_arr[i][j+k+1] == 0:
                    t_cnt += 1

    print(f'#{tc} {t_cnt}')