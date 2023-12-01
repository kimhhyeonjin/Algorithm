import sys

# 방향 동남서북
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# 가로A, 세로B
A, B = map(int, input().split())
# 로봇수 N, 명령수 M
N, M = map(int, input().split())
# 땅
land = [[0] * A for _ in range(B)]
# 각 로봇의 초기 위치 및 방향
robots = []
for i in range(N):
    y, x, dd = input().split()
    if dd == 'E':
        robots.append([[B-int(x), int(y)-1], 0])
    elif dd == 'S':
        robots.append([[B-int(x), int(y)-1], 1])
    elif dd == 'W':
        robots.append([[B-int(x), int(y)-1], 2])
    else:
        robots.append([[B-int(x), int(y)-1], 3])
    land[B-int(x)][int(y)-1] = i + 1
# 명령
simul = 0
for _ in range(M):
    robot, o, r = input().split()
    robot_num = robots[int(robot)-1]
    if o == 'L':
        robot_num[1] = (robot_num[1] + 3 * int(r)) % 4
    elif o == 'R':
        robot_num[1] = (robot_num[1] + 1 * int(r)) % 4
    else:
        for _ in range(int(r)):
            di = robot_num[0][0] + d[robot_num[1]][0]
            dj = robot_num[0][1] + d[robot_num[1]][1]
            # Robot X crashes into the wall
            if di < 0 or di >= B or dj < 0 or dj >= A:
                simul = [1, robot]
                break
            # Robot X crashes into robot Y
            if land[di][dj] != 0:
                simul = [2, robot, land[di][dj]]
                break
            # 정상작동
            land[robot_num[0][0]][robot_num[0][1]] = 0
            robot_num[0][0] = di
            robot_num[0][1] = dj
            land[di][dj] = robot
    if simul != 0:
        break
if simul == 0:
    print('OK')
elif simul[0] == 1:
    print('Robot', simul[1], 'crashes into the wall')
else:
    print('Robot', simul[1], 'crashes into robot', simul[2])