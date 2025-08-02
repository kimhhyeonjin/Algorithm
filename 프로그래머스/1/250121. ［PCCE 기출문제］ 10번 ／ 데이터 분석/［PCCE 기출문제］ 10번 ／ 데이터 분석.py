def solution(data, ext, val_ext, sort_by):
    answer = []
    ex = ["code", "date", "maximum", "remain"]
    for d in range(len(data)):
        if data[d][ex.index(ext)] < val_ext:
            answer.append(data[d])
    
    answer.sort(key = lambda x : x[ex.index(sort_by)])
    return answer