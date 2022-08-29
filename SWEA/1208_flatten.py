import sys
sys.stdin = open('1208_flatten.txt')

T = 10  # 테스트 케이스의 개수

for i in range(1, T+1):
    dump = int(input())  # 케이스 별 덤프의 횟수
    boxes = list(map(int, input().split()))  # 가로 길이 100개의 높이를 리스트로


    while dump:  # dump가 1이상이면 아래를 실행
        max_idx = 0   # 초기화를 위해 while문 아래 입력
        min_idx = 0
        max_box = boxes[0]
        min_box = boxes[0]
        for j in range(100):
            if max_box < boxes[j]:  # 최대값을 찾고
                max_box = boxes[j]
                max_idx = j
            if min_box > boxes[j]:  # 최소값을 찾아
                min_box = boxes[j]
                min_idx = j
        boxes[max_idx] -= 1  # 최대값을 1만큼 줄이고
        boxes[min_idx] += 1  # 최소값을 1만큼 늘이는 과정을
        dump -= 1  # dump가 0이 될 때까지 반복

    # 평탄화 후의 최대값과 최소값의 차이를 구하기 위해 위의 과정을 한 번 더 반복
    max_box = boxes[0]
    min_box = boxes[0]
    for j in range(100):
        if max_box < boxes[j]:
            max_box = boxes[j]
        if min_box > boxes[j]:
            min_box = boxes[j]

    print(f'#{i} {max_box - min_box}')