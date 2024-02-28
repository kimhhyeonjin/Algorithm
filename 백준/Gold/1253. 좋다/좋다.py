n = int(input())
if n == 1 or n == 2:
    print(0)
else:
    numbers = list(map(int, input().split()))
    numbers.sort()

    cnt = 0
    # 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”
    for i in range(len(numbers)):
        goal = numbers[i]
        num_list = numbers[:i] + numbers[i+1:]
        s, e = 0, len(num_list)-1
        while s < e:
            if num_list[s] + num_list[e] == goal:
                cnt += 1
                break
            if num_list[s] + num_list[e] < goal:
                s += 1
            else:
                e -= 1
    print(cnt)