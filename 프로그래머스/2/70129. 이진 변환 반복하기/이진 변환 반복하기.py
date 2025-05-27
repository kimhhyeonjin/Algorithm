def solution(s):
    c, z = 0, 0
    while s != "1":
        z += s.count("0")
        s = bin(s.count("1"))[2:]
        c += 1
    answer = [c, z]
    return answer