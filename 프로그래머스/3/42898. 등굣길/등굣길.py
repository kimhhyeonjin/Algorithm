def solution(m, n, puddles):
    road = [[0] * m for _ in range(n)]
    road[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles:
                continue
            elif i == 0:
                if j != 0:
                    road[i][j] += road[i][j - 1]
            elif j == 0:
                road[i][j] += road[i - 1][j]
            else:
                road[i][j] += road[i - 1][j] + road[i][j - 1]
    
    answer = road[-1][-1] % 1000000007
    return answer