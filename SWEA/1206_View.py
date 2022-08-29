import sys
sys.stdin = open('1206_View.txt')

N = 10

for i in range(N):  # 테스트케이스 갯수
    building_num = int(input())  # 각 테스트에서 건물 갯수
    building = list(map(int, input().split()))  # 건물의 각 높이를 리스트로
    count = 0  # 갯수 세기 위해서
    building_max = 0  # 주변 건물의 최대 높이
    for j in range(2, building_num-2):  # range 설정 확인하기
        building_max = building[j-2]
        for k in [j-2, j-1, j+1, j+2]:
            if building_max < building[k]:
                building_max = building[k]
        if building[j] > building_max:
            count += (building[j] - building_max)

    print(f'#{i+1} {count}')


# 또 다른 방법

# import sys
# sys.stdin = open('SWEA_1206.txt')
#
# for tc in range(1, 11):  # 문제의 개수
#     cnt = int(input())  # 빌딩 수
#     building_list = list(map(int, input().split()))  # 빌딩 목록
#
#     result = 0
#     for i in range(cnt):
#         cur_building = building_list[i]
#
#         if not cur_building:  # 빌딩이 없는 경우 좌우 확인 안해도 됨
#             continue
#         else:
#             max_height = 0
#             idx = [-2, -1, 1, 2] : 좌, 우 2칸 idx
#             for side in range(4):  # 좌우 2칸씩 총 4번 비교
#                 if building_list[i + idx[side]] > max_height:  # 가장 높은 빌딩
#                     max_height = building_list[i + idx[side]]
#
#             if cur_building > max_height:  # 현재 빌딩과 가장 높은 좌우 빌딩 비교
#                 result += cur_building - max_height
#
#     print(f'#{tc} {result}')