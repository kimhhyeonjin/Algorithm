def solution(n, stations, w):
    answer = 0
    cur = 0
    i = 0

    while cur < n:
        if i < len(stations) and stations[i] - w <= cur + 1:
            cur = stations[i] + w
            i += 1
        else:
            answer += 1
            cur = cur + 2 * w + 1
    
    return answer