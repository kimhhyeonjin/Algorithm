def solution(arr1, arr2):
    answer = []
    a, b, c = len(arr1), len(arr2), len(arr2[0])
    
    for i in range(a):
        temp = []
        for j in range(c):
            t = 0
            for k in range(b):
                t += arr1[i][k] * arr2[k][j]
            temp.append(t)
        answer.append(temp)
    return answer