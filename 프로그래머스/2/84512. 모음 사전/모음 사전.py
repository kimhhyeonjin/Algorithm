def solution(word):
    answer = 0
    vowel = ["A", "E", "I", "O", "U"]
    
    for w in range(len(word)):
        for v in range(len(vowel)):
            if word[w] == vowel[v]:
                answer += 1
                break
            else:
                temp = 0
                for i in range(5 - w):
                    temp = temp * 5 + 1
                answer += temp
    return answer