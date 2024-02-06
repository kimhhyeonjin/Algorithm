def switching(cur, start, end, cnt):
    if start == 0:
        cnt += 1
        cur[0] = (cur[0] + 1) % 2
        cur[1] = (cur[1] + 1) % 2
    for i in range(1, end):
        if cur[i-1] != goal[i-1]:
            cnt += 1
            cur[i-1] = (cur[i-1] + 1) % 2
            cur[i] = (cur[i] + 1) % 2
            if i != end-1:
                cur[i+1] = (cur[i+1] + 1) % 2
    else:
        if cur == goal:
            return cnt
        else:
            return -1

n = int(input())
# 0부터 시작
cur0 = list(map(int, input()))
# 1부터 시작
cur1 = cur0[:]
goal = list(map(int, input()))

res0 = switching(cur0, 0, n, 0)
res1 = switching(cur1, 1, n, 0)

if res0 >= 0 and res1 >= 0:
    print(min(res0, res1))
elif res0 < 0 and res1 < 0:
    print(res0)
else:
    print(max(res0, res1))