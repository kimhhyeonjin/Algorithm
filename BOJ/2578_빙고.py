'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''

bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))
# print(bingo)

match = []
for _ in range(5):
    match.append(list(map(int, input().split())))
# print(match)

cnt = 0
for i in range(5):
    for j in range(5):
        num = match[i][j]
        for m in range(5):
            for n in range(5):
                if bingo[m][n] == num:
                    bingo[m][n] = 0
                    cnt += 1

        res = 0
        for a in range(5):
            if bingo[a] == [0, 0, 0, 0, 0]:
                res += 1

        diag_cnt = 0
        for a in range(5):
            if bingo[a][a] == 0:
                diag_cnt += 1
            else:
                break
        if diag_cnt == 5:
            res += 1

        diag_cnt = 0
        for a in range(5):
            if bingo[a][5-a-1] == 0:
                diag_cnt += 1
            else:
                break
        if diag_cnt == 5:
            res += 1

        for a in range(5):
            diag_cnt = 0
            for b in range(5):
                if bingo[b][a] == 0:
                    diag_cnt += 1
                else:
                    break
            if diag_cnt == 5:
                res += 1
        if res >= 3:
            print(cnt)
            break
    if res >= 3:
        break