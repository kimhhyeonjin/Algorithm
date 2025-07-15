def solution(lottos, win_nums):
    lotto = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}
    
    cnt = 0
    for l in lottos:
        if l in win_nums:
            cnt += 1
    
    answer = [lotto[cnt + lottos.count(0)], lotto[cnt]]
    return answer