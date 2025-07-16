def solution(x, y, n):
    l = [10000000] * (y + 1)
    l[x] = 0
    for i in range(y):
        if i + n <= y:
            l[i + n] = min(l[i + n], l[i] + 1)
        if 2 * i <= y:
            l[2 * i] = min(l[2 * i], l[i] + 1)
        if 3 * i <= y:
            l[3 * i] = min(l[3 * i], l[i] + 1)
    
    answer = l[-1] if l[-1] < 10000000 else -1
    return answer