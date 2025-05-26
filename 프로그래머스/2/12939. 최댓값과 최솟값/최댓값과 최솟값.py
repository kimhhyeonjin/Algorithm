def solution(s):
    new_s = list(map(int, s.split()))
    m_v = [str(min(new_s)), str(max(new_s))]
    answer = " ".join(m_v)
    return answer