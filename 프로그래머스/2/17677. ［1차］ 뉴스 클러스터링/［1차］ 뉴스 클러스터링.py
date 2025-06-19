def solution(str1, str2):
    n_str1 = str1.lower()
    s1 = {}
    for i in range(len(n_str1) - 1):
        if n_str1[i:i+2].isalpha():
            if n_str1[i:i+2] not in s1:
                s1[n_str1[i:i+2]] = 0
            s1[n_str1[i:i+2]] += 1
    
    n_str2 = str2.lower()
    s2 = {}
    for i in range(len(n_str2) - 1):
        if n_str2[i:i+2].isalpha():
            if n_str2[i:i+2] not in s2:
                s2[n_str2[i:i+2]] = 0
            s2[n_str2[i:i+2]] += 1
    
    if len(s1) == 0 and len(s2) == 0:
        result = 1
    else:
        t = []
        for i in s1:
            if i not in s2:
                s2[i] = s1[i]
                t.append(i)
            else:
                s1[i], s2[i] = min(s1[i], s2[i]), max(s1[i], s2[i])
        for i in t:
            s1.pop(i)
        
        a, b = 0, 0
        for i in s1:
            a += s1[i]
        for i in s2:
            b += s2[i]
        result = a / b
        
    answer = int(result * 65536)
    return answer