import sys
sys.stdin = open('1970_쉬운거스름돈.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    mon = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    stack = []
    for i in mon:
        stack.append(N // i)
        N = N - i * (N // i)
    print(f'#{tc}')
    print(*stack)