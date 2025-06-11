def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for c in cities:
        c = c.lower()
        if c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        else:
            if cacheSize:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(c)
            answer += 5
    
    return answer