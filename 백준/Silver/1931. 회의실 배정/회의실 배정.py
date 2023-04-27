N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# arr을 시작하는 시간을 기준으로 오름차순 정렬
arr.sort(key=lambda x:x[0])
# arr을 끝나는 시간을 기준으로 오름차순 정렬
arr.sort(key=lambda x: x[1])
# print(arr)

cnt = 0
compare = 0
for i in range(N):
    if compare <= arr[i][0]:
        compare = arr[i][1]
        cnt += 1
    else:
        continue
print(cnt)