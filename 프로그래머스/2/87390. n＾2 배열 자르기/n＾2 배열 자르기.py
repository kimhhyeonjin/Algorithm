def solution(n, left, right):
    answer = []
    n_left = [left // n, left % n]
    n_right = [right // n, right % n]
    
    for i in range(n_left[0], n_right[0] + 1):
        for j in range(n):
            if i == n_left[0]:
                if j < n_left[1]:
                    continue
            if i == n_right[0]:
                if j > n_right[1]:
                    break
            answer.append(max(i, j) + 1)
    return answer