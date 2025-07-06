from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    min_heap = []
    for s in scoville:
        heappush(min_heap, s)
    
    while min_heap[0] < K:
        if len(min_heap) == 1:
            answer = -1
            break
        a = heappop(min_heap)
        b = heappop(min_heap)
        heappush(min_heap, a + b * 2)
        answer += 1
        
    return answer