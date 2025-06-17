def solution(nums):
    n = set()
    num = [i for i in range(sum(nums) + 1)]
    for i in range(2, sum(nums) + 1):
        if num[i]:
            n.add(num[i])
            for j in range(i, sum(nums) + 1, i):
                num[j] = 0
    
    answer = 0
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] in n:
                    answer += 1
    return answer