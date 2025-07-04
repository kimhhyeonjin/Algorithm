def solution(msg):
    answer = []
    idx_num = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    idx = 0
    while idx < len(msg):
        cnt = 1
        while msg[idx : idx + cnt] in idx_num:
            cnt += 1
            if idx + cnt == len(msg) + 1:
                break
        cnt -= 1
        answer.append(idx_num.index(msg[idx : idx + cnt]) + 1)
        idx_num.append(msg[idx : idx + cnt + 1])
        idx += cnt
        
    return answer