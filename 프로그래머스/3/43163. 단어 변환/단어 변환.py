from collections import deque

def solution(begin, target, words):
    answer = 100
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    visited = [0] * len(words)
    
    q = deque()
    q.append([begin, 0])
    while q:
        w, c = q.popleft()
        if w == target:
            if answer > c:
                answer = c
                return answer
        for i in range(len(w)):
            for a in alphabet:
                n = w[:i] + a + w[i+1:]
                if n != w and n in words:
                    for j in range(len(words)):
                        if n == words[j] and not visited[j]:
                            visited[j] = 1
                            q.append([words[j], c + 1])
    if answer == 100:
        return 0