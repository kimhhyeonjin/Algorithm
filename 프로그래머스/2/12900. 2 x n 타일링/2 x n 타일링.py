def solution(n):
    dp = [0] * 100000
    dp[1] = 1
    dp[2] = 2
    
    if n >= 3:
        for d in range(3, n + 1):
            dp[d] = (dp[d-1] + dp[d-2]) % 1000000007
    return dp[n]