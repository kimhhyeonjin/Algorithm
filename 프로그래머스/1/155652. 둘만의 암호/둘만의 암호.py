def solution(s, skip, index):
    answer = ''
    sk = []
    for p in skip:
        sk.append(ord(p))
    
    for st in s:
        ns = ord(st)
        cnt = 0
        while cnt < index:
            ns += 1
            if ns > ord('z'):
                ns -= 26
            while ns in sk:
                ns += 1
                if ns > ord('z'):
                    ns -= 26
            cnt += 1
        answer += chr(ns)
    return answer