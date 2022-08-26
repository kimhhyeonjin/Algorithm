R, C = map(int, input().split())
N = int(input())
for _ in range(C):
    arr = [[0] * R]

cut = []
for _ in range(N):
    cut.append(list(map(int, input().split())))
# print(cut)

r_cut = []
c_cut = []
for i in range(N):
    # 가로
    if cut[i][0] == 0:
        r_cut.append(cut[i][1])
    # 세로
    elif cut[i][0] == 1:
        c_cut.append(cut[i][1])
# 위의 두 함수가 정렬되어있지 않을 수 있음
r_cut.sort()  # .sort() 함수를 사용하면 리스트 자체가 sort됨
c_cut.sort()
# print(r_cut)
# print(c_cut)

max_area = 0
r_cut = [0] + r_cut + [C]
c_cut = [0] + c_cut + [R]
for x in range(1, len(r_cut)):
    for y in range(1, len(c_cut)):
        area = (r_cut[x] - r_cut[x-1]) * (c_cut[y] - c_cut[y-1])
        # print(area)
        if max_area < area:
            max_area = area
print(max_area)