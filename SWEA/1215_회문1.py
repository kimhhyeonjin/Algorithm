import sys
sys.stdin = open('1215_회문1.txt')

for tc in range(1, 11):
    N = int(input())
    arr = []
    for _ in range(8):
        arr.append(input())

    # 가로
    cnt = 0
    for i in range(8):
        for j in range(8 - N + 1):
            text_r = arr[i][j:j+N]
            if text_r == text_r[::-1]:
                cnt += 1

    # 세로
    for i in range(8):
        for j in range(8 - N + 1):
            text_c = ''
            for k in range(N):
                text_c += arr[j+k][i]
            if text_c == text_c[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')