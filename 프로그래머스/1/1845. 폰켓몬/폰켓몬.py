def solution(nums):
    num = len(nums) // 2
    chk = {}
    
    for i in nums:
        if i in chk:
            chk[i] += 1
        else:
            chk[i] = 1
    
    if len(chk) >= num:
        answer = num
    else:
        answer = len(chk)
    
    return answer