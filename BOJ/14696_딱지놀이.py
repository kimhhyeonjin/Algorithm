T = int(input())

for _ in range(T):
    num_a, *play_a = map(int, input().split())
    num_b, *play_b = map(int, input().split())
    # num은 정수형태, play는 list형태

    # 버블소트를 이용하여 역순정렬
    for i in range(num_a-1, 0, -1):
        for j in range(i):
            if play_a[j] < play_a[j+1]:
                play_a[j], play_a[j+1] = play_a[j+1], play_a[j]
    
    for i in range(num_b-1, 0, -1):
        for j in range(i):
            if play_b[j] < play_b[j+1]:
                play_b[j], play_b[j+1] = play_b[j+1], play_b[j]
    # print(play_a, play_b)

    round = num_a
    if num_a > num_b:
        round = num_b
    
    for playnum in range(round):
        if play_a[playnum] > play_b[playnum]:
            print('A')
            break
        elif play_a[playnum] < play_b[playnum]:
            print('B')
            break
    else:  # for문이 break 등으로 끊기지 않았을 때 실행
        if play_a > play_b:
            print('A')
        elif play_a < play_b:
            print('B')
        else:
            print('D')