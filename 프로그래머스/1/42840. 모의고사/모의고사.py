def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    for i in range(len(answers)):
        if s1[i % len(s1)] == answers[i]:
            score[0] += 1
        if s2[i % len(s2)] == answers[i]:
            score[1] += 1
        if s3[i % len(s3)] == answers[i]:
            score[2] += 1
    
    max_s = max(score)
    for j in range(3):
        if score[j] == max_s:
            answer.append(j+1)
    
    return answer