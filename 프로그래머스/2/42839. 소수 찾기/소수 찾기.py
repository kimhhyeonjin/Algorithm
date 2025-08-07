from itertools import permutations

def solution(numbers):
    answer = 0
    numbers_list = []
    numbers_set = set()

    for i in range(1, len(numbers) + 1):
        numbers_list += (list(permutations(numbers, i)))
    
    for i in numbers_list:
        temp = ""
        for j in i:
            temp += j
        numbers_set.add(int(temp))
    
    for num in numbers_set:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                answer += 1
    
    return answer