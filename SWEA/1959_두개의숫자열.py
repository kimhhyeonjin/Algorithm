import sys
sys.stdin = open('1959_두개의숫자열.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    stack = []
    if N > M:
        for i in range(N - M + 1):
            total = 0
            for j in range(M):
                total += A[i+j] * B[j]
            stack.append(total)

    if N == M:
        total = 0
        for i in range(N):
            total += A[i] * B[i]
        stack.append(total)

    if N < M:
        for i in range(M - N + 1):
            total = 0
            for j in range(N):
                total += A[j] * B[i+j]
            stack.append(total)

    print(f'#{tc} {max(stack)}')