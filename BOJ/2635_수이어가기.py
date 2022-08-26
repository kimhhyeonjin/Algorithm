N = int(input())
length = 0

# N이 1인 경우와 아닌 경우로 나누어 계산
if N == 1:
    print(4)
    print(1, 1, 0, 1)
else:
    for i in range(1, N):
    # 두번째 수가 N보다 큰 경우, 세번째 수가 음수이므로 최대 길이는 2
        num = [N, i]
        # print(num)

        while True:
            new = num[-2] - num[-1]
            if new >= 0:
                num.append(new)
            else:
                break

        if length < len(num):
            length = len(num)
            num_list = num

    print(length)
    print(*num_list)