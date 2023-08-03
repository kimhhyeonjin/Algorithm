def solution(m, n, puddles):
    arr = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles:
                continue
            elif i ==  0:
                if j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i][j-1]
            elif j == 0:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
            
    answer = arr[n-1][m-1] % 1000000007
    return answer