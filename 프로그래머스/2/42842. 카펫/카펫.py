def solution(brown, yellow):
    for c in range(1, brown + yellow):
        if (brown + yellow) % c == 0:
            r = (brown + yellow) // c
            if (c - 2) * (r - 2) == yellow:
                answer = [r, c]
                break
    return answer