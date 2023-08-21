import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
fixed = [int(sys.stdin.readline().strip()) for _ in range(M)]

# 1번이 고정석이 아닌 경우
# 0번을 고정석이라고 생각
if 1 not in fixed:
    fixed = [0] + fixed
# N번이 고정석이 아닌 경우
# N+1번을 고정석이라고 생각
if N not in fixed:
    fixed = fixed + [N+1]

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1
if N >= 2:
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]

cnt = 1
for i in range(len(fixed)-1):
    # (fixed[i+1]-fixed[i]-1)개만큼 자유롭게 배치 가능
    cnt *= dp[fixed[i+1]-fixed[i]-1]
print(cnt)