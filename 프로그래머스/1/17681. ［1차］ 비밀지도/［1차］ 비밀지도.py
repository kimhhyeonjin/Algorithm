def solution(n, arr1, arr2):
    answer = []
    
    for a in range(n):
        a1 = '0' * (n - len(bin(arr1[a])[2:])) + bin(arr1[a])[2:]
        a2 = '0' * (n - len(bin(arr2[a])[2:])) + bin(arr2[a])[2:]
        temp = ''
        for i in range(n):
            if a1[i] == '0' and a2[i] == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer