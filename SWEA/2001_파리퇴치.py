import sys
sys.stdin = open('2001_파리퇴치.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    wall = [list(map(int, input().split())) for _ in range(N)]
    # print(wall)

    max_fly = 0
    for i in range(N - M + 1):
        for m in range(N - M + 1):
            cnt = 0
            for j in range(M):
                for n in range(M):
                    cnt += wall[i+j][m+n]
            if max_fly < cnt:
                max_fly = cnt
    print(f'#{tc} {max_fly}')