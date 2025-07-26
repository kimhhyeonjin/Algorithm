def solution(X, Y):
    # 방법1
    answer = ""
    for i in range(9, -1, -1):
        answer += str(i) * min(X.count(str(i)), Y.count(str(i)))
        
    if not answer:
        answer = "-1"
    elif len(answer) == answer.count("0"):
        answer = "0"
    
    # 방법2
    # x_cnt = {}
    # y_cnt = {}
    # for x in X:
    #     if x not in x_cnt:
    #         x_cnt[x] = 1
    #     else:
    #         x_cnt[x] += 1
    # for y in Y:
    #     if y in x_cnt:
    #         x_cnt[y] -= 1
    #         if x_cnt[y] == 0:
    #             del x_cnt[y]
    #         if y not in y_cnt:
    #             y_cnt[y] = 1
    #         else:
    #             y_cnt[y] += 1
    
    # if not y_cnt:
    #     answer = "-1"
    # elif len(y_cnt) == 1 and "0" in y_cnt:
    #     answer = "0"
    # else:
    #     p = []
    #     for y in y_cnt:
    #         p += [y] * y_cnt[y]
    #     p.sort(reverse = True)
    #     answer = ''.join(p)
    
    return answer