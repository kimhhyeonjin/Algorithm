def solution(elements):
    num = set()
    c_elements = elements + elements
    for i in range(len(elements)):
        for j in range(len(elements)):
            n = sum(c_elements[i : i+j+1])
            num.add(n)
    
    answer = len(num)
    return answer