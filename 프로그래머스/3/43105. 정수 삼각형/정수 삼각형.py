def solution(triangle):
    # 방법1
    # num = [0] * (len(triangle) + 1)
    # num[0] = triangle[0][0]
    
    # if len(triangle) > 1:
    #     for tri in range(1, len(triangle)):
    #         temp = num[:]
    #         for t in range(len(triangle[tri]) - 1):
    #             if temp[t] + triangle[tri][t] > num[t]:
    #                 num[t] = temp[t] + triangle[tri][t]
    #             if temp[t] + triangle[tri][t+1] > num[t+1]:
    #                 num[t+1] = temp[t] + triangle[tri][t+1]
    # answer = max(num)
    
    # 방법2
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    answer = max(triangle[-1])
    
    return answer