def solution(k, tangerine):
    answer = 0
    chk = [0] * 100000000
    for t in tangerine:
        chk[t] += 1
    chk.sort(reverse = True)
    cnt = 0
    for c in range(len(chk)):
        cnt += chk[c]
        answer += 1
        if cnt >= k:
            break
    return answer