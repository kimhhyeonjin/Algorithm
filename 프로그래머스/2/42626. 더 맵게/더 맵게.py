from heapq import heappush, heappop

def solution(scoville, K):
    h = []
    for i in scoville:
        heappush(h, i)
    
    answer = 0
    while h[0] < K and len(h) > 1:
        f = heappop(h)
        s = heappop(h)
        heappush(h, f + 2*s)
        answer += 1
    
    if h[0] < K:
        answer = -1
    return answer