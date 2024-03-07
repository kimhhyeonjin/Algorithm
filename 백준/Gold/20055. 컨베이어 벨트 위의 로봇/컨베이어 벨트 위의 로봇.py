from  collections import deque

times = 0
n, k = map(int, input().split())
a = list(map(int, input().split()))
c = deque(a)            # 컨베이어벨트
r = deque([0] * n)      # 로봇

while True:
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    temp_c = c.pop()
    c.appendleft(temp_c)
    r.pop()
    r.appendleft(0)
    r[-1] = 0
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    # 만약 이동할 수 없다면 가만히 있는다.
    if sum(r):
        for i in range(n-2, -1, -1):
            if r[i] == 1 and r[i+1] == 0 and c[i+1] > 0:
                r[i] = 0
                r[i+1] = 1
                c[i+1] -= 1
    r[-1] = 0
    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if c[0] > 0:
        c[0] -= 1
        r[0] = 1
    # 내구도가 0인 칸의 개수가 k개 이상이라면 과정을 종료
    times += 1
    if c.count(0) >= k:
        break

print(times)