import heapq

def solution(n, works):
    answer = 0
    if sum(works) >= n:
        max_heap = []
        for w in works:
            heapq.heappush(max_heap, -w)
        while n:
            temp = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -(temp - 1))
            n -= 1
        
        total = 0
        for i in max_heap:
            total += i ** 2
        answer += total
    return answer