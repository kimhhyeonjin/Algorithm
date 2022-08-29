import sys
sys.stdin = open('1209_Sum.txt')

T = 10
for i in range(1, T+1):
    n = int(input())  # 각 테스트 케이스의 번호
    arr = [list(map(int, input().split())) for _ in range(100)]  # 100x100 크기의 2차원 배열로 표현
    # pythonic
    max_sum = 0  # 합의 최대값
    for a in range(100):
        row_sum = column_sum = ldiag_sum = rdiag_sum = 0
        for b in range(100):
            row_sum += arr[a][b]  # 행의 합
            column_sum += arr[b][a]  # 열의 합
        if max_sum < row_sum:
            max_sum = row_sum  # 행의 합이 기존의 최대값보다 크면 대체
        if max_sum < column_sum:
            max_sum = column_sum  # 열의 합이 기존의 최대값보다 크면 대체
        ldiag_sum += arr[a][a]  # 왼쪽 대각선의 합
        rdiag_sum += arr[a][99-a]  # 오른쪽 대각선의 합
        if max_sum < ldiag_sum:
            max_sum = ldiag_sum  # 왼쪽 대각선의 합이 기존의 최대값보다 크면 대체
        if max_sum < rdiag_sum:
            max_sum = rdiag_sum  # 오른쪽 대각선의 합이 기존의 최대값보다 크면 대체
    print(f'#{i} {max_sum}')  # 최대값 출력


#####################################################################################################################
# 또 다른 방법
# import sys
# sys.stdin = open('SWEA_1209.txt')
#
# for tc in range(10):
#     N = input()  # 테스트 케이스 숫자
#
#     numbers = []
#     for _ in range(100):
#         numbers.append(list(map(int, input().split())))  # 100개의 원소를 가지는 리스트
#
#     # 가로합
#     max_value = 0
#     for i in range(100):
#         my_total = 0
#         for j in range(100):
#             my_total += numbers[i][j]
#
#         if max_value < my_total:
#             max_value = my_total
#
#     # 세로합
#     for i in range(100):
#         my_total = 0
#         for j in range(100):
#             my_total += numbers[j][i]
#
#         if max_value < my_total:
#             max_value = my_total
#
#     # 좌측 상단에서 내려오는 대각선합
#     my_total = 0
#     for i in range(100):
#         my_total += numbers[i][i]
#
#         if max_value < my_total:
#             max_value = my_total
#
#     # 우측 상단에서 내려오는 대각선합
#     my_total = 0
#     for i in range(100):
#         my_total += numbers[i][99-i]
#
#         if max_value < my_total:
#             max_value = my_total