def solution(cards1, cards2, goal):
    answer = 'No'
    i, j = 0, 0
    for g in goal:
        if i < len(cards1) and cards1[i] == g:
            i += 1
        elif j < len(cards2) and cards2[j] == g:
            j += 1
        else:
            break
    else:
        answer = 'Yes'
    return answer