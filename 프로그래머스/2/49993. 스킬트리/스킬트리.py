def solution(skill, skill_trees):
    answer = 0
    
    for trees in skill_trees:
        i = 0
        for t in trees:
            if t in skill:
                if t == skill[i]:
                    i += 1
                    if i == len(skill):
                        answer += 1
                        break
                else:
                    break
        else:
            answer += 1

    return answer