from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    
    user = defaultdict(int)
    for i in range(len(want)):
        user[want[i]] = number[i]
    
    market = defaultdict(int)
    for j in range(len(discount)):
        if j >= 10:
            market[discount[j - 10]] -= 1
            market[discount[j]] += 1
        elif j == 9:
            market[discount[j]] += 1
        if j >= 9:
            for w in want:
                if user[w] != market[w]:
                    break
            else:
                answer += 1
        else:
            market[discount[j]] += 1
    
    return answer