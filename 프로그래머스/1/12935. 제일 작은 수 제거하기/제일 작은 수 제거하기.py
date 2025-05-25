def solution(arr):
    if len(arr) == 1:
        answer = [-1]
    else:
        min_arr = min(arr)
        for i in range(len(arr)):
            # 시간초과
            # if arr[i] == min(arr):
            if arr[i] == min_arr:
                arr.pop(i)
                answer = arr
                break
    return answer