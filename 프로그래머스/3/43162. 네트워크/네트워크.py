from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            answer += 1
            q = deque()
            q.append(i)
            while q:
                j = q.pop()
                for k in range(n):
                    if computers[j][k] and not visited[k]:
                        visited[k] = 1
                        q.append(k)
    return answer