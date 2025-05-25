def solution(s):
    # 방법1
    new_s = sorted(s)
    new_s.sort(reverse = True)
    answer = ''.join(new_s)
    
    # 방법2
    # new_s = list(s)
    # for i in range(len(new_s)):
    #     new_s[i] = ord(new_s[i])
    # new_s.sort(reverse = True)
    # for i in range(len(new_s)):
    #     new_s[i] = chr(new_s[i])
    # answer = ''.join(new_s)
    return answer