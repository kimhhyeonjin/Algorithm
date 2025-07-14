def solution(fees, records):
    answer = []
    
    car_io = {}
    car_time = {}
    for rec in records:
        t, n, s = rec.split(" ")
        if n not in car_io:
            car_io[n] = 0
            car_time[n] = 0
        h, m = list(map(int, t.split(":")))
        if s == "IN":
            car_io[n] = 1
            car_time[n] -= (h * 60 + m)
        else:
            car_io[n] = 0
            car_time[n] += (h * 60 + m)
    for c in car_io:
        if car_io[c]:
            car_time[c] += (23 * 60 + 59)
    
    fee_list = []
    for c in car_time:
        if car_time[c] > fees[0]:
            additional_time = car_time[c] - fees[0]
            if additional_time % fees[2] == 0:
                fee_list.append([c, fees[1] + additional_time // fees[2] * fees[3]])
            else:
                fee_list.append([c, fees[1] + (additional_time // fees[2] + 1) * fees[3]])
        else:
            fee_list.append([c, fees[1]])
    
    fee_list.sort()
    for f in fee_list:
        answer.append(f[1])
    return answer