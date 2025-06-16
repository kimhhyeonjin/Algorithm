# 나중에 다른 방법으로 다시 풀어보기
def solution(n, m, section):
    answer = 0
    
    i = 1
    s = 0
    flag = True
    while flag:
        if i < section[s]:
            i = section[s]
        i += (m - 1)
        answer += 1
        for se in range(s, len(section)):
            if section[se] > i:
                s = se
                break
            if se == len(section) - 1:
                flag = False
    return answer