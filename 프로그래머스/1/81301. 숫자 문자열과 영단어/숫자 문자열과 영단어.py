def solution(s):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for n in range(len(num)):
        if num[n] in s:
            s = s.replace(num[n], str(n))
    
    answer = int(s)
    return answer