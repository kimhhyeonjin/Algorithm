def solution(x):
    new_x = map(int, str(x))
    # new_x = list(map(int, str(x)))
    if x % sum(new_x) == 0:
        answer = True
    else:
        answer = False
    return answer