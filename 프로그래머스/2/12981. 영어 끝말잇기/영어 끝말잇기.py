def solution(n, words):
    answer = []
    spoken_words = []
    
    for w in range(len(words)):
        if w == 0:
            spoken_words.append(words[w])
        elif words[w] in spoken_words or spoken_words[-1][-1] != words[w][0]:
            answer = [(w % n) + 1, (w // n) + 1]
            break
        else:
            spoken_words.append(words[w])
    else:
        answer = [0, 0]    

    return answer