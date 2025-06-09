def solution(a, b):
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    cnt = 0
    for i in range(a-1):
        cnt += months[i]
    cnt += b
    
    answer = days[(cnt + 4) % 7]
    return answer