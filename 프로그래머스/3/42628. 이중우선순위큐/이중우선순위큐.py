import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    removed = set()
    count = {}

    for op in operations:
        command = op.split()
        
        if command[0] == "I":
            num = int(command[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            
            if num not in count:
                count[num] = 0
            count[num] += 1
            
        elif command[0] == "D":
            if command[1] == "1":
                while max_heap and (-max_heap[0] in removed or count[-max_heap[0]] == 0):
                    popped_val = -heapq.heappop(max_heap)
                    removed.add(popped_val)
                
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    count[max_val] -= 1
                    
            elif command[1] == "-1":
                while min_heap and (min_heap[0] in removed or count[min_heap[0]] == 0):
                    popped_val = heapq.heappop(min_heap)
                    removed.add(popped_val)
                
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    count[min_val] -= 1

    while min_heap and (min_heap[0] in removed or count[min_heap[0]] == 0):
        heapq.heappop(min_heap)
        
    while max_heap and (-max_heap[0] in removed or count[-max_heap[0]] == 0):
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        return [0, 0]
    
    return [-max_heap[0], min_heap[0]]
