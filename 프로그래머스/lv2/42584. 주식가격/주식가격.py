def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                # 1초 뒤에 가격이 떨어지므로
                # 1만큼을 더해줌
                cnt += 1
                break
        answer[i] += cnt
    return answer