import sys

N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()

# 이분탐색
low = 0
high = house[-1] - house[0]
while low <= high:
    # mid는 공유기 거리
    mid = (low + high) // 2
    # 첫번째 집 선택
    current = house[0]
    cnt = 1
    # current를 기준으로 mid값 이상에 위치한 곳에 공유기 설치
    for i in range(1, N):
        if house[i] >= current + mid:
            # 공유기 설치
            cnt += 1
            current = house[i]
    # 주어진 C보다 공유기 설치를 많이 했으므로 공유기 거리를 늘려 최대 거리 찾기
    if cnt >= C:
        low = mid + 1
        # 현재의 공유기 거리 저장
        result = mid
    else:
        high = mid - 1
print(result)