def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        i, j, k = commands[c]
        c_list = array[i-1:j]
        c_list.sort()
        answer.append(c_list[k-1])
    return answer