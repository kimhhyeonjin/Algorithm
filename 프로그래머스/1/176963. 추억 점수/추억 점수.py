def solution(name, yearning, photo):
    answer = []
    
    score = {}
    for n in range(len(name)):
        score[name[n]] = yearning[n]
    
    for ph in photo:
        point = 0
        for p in ph:
            if p in score:
                point += score[p]
        answer.append(point)
    return answer