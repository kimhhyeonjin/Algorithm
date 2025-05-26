def solution(price, money, count):
    cnt = 1
    while cnt <= count:
        money -= cnt * price
        cnt += 1
    if money >= 0:
        answer = 0
    else:
        answer = -1 * money

    return answer