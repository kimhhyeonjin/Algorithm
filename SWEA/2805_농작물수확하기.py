import sys
sys.stdin = open('2805_농작물수확하기.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = []
    for _ in range(N):
        farm.append(input())

    crop = 0
    for i in range(N // 2 + 1):
        for j in range(-i, i+1):
            crop += int(farm[i][N // 2 + j])
    # print(crop)

    for i in range(N // 2 + 1, N):
        # 구현력 기르는 연습 필요
        for j in range((i - N) + 1, N - i):
            crop += int(farm[i][N // 2 + j])
    print(f'#{tc} {crop}')