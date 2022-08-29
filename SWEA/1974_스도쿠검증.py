import sys
sys.stdin = open('1974_스도쿠검증.txt')

T = int(input())

for tc in range(1, T+1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    # print(arr)

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 0
    # 칸
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            cnt = [0] * 9
            for m in range(3):
                for n in range(3):
                    cnt[arr[i+m][j+n]-1] += 1
            # print(cnt)
            if 0 in cnt:
            # if [0] in cnt:하면 리스트 안에 [0]이 있는지 확인하는 것이므로 항상 false
                result += 1
    # print(result)

    # 가로 & 세로
    for i in range(9):
        cnt_r = [0] * 9
        cnt_c = [0] * 9
        for j in range(9):
            cnt_r[arr[i][j] - 1] += 1
            cnt_c[arr[j][i] - 1] += 1
        if 0 in cnt_r or 0 in cnt_c:
            result += 1
    # print(result)

    if result > 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')