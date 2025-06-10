from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    dungeon_list = list(permutations(dungeons, len(dungeons)))
    for dl in dungeon_list:
        kk = k
        cnt = 0
        for d in dl:
            if kk >= d[0]:
                kk -= d[1]
                cnt += 1
        else:
            if answer < cnt:
                answer = cnt
            
    return answer