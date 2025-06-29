def base(i, n):
    w = ''
    ch = ['A', 'B', 'C', 'D', 'E', 'F']
    if i == 0:
        w = '0'
    while i:
        temp = i % n
        if temp >= 10:
            w += ch[temp % 10]
        else:
            w += str(temp)
        i //= n
    w = w[::-1]
    return w

def solution(n, t, m, p):
    answer = ''
    num = ''
    i = 0
    
    while len(num) < (t + 1) * m:
        num += base(i, n)
        i += 1
    
    for i in range(p - 1, (t - 1) * m + p, m):
        answer += num[i]
    return answer