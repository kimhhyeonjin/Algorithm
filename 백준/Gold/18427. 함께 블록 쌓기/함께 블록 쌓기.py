# def dfs(start, depth, cur, height):
#     global cnt
#     if cur > height:
#         return
#     if start == depth:
#         if cur == height:
#             cnt += 1
#         return
#     for i in range(len(blocks[start])):
#         dfs(start+1, n, cur+blocks[start][i], height)

n, m, h = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(n)]

# cnt = 0
# dfs(0, n, 0, h)
dp = [[1] + [0]*h for _ in range(n+1)]      # 높이가 0인 경우 값을 1로 두고 dp 계산
for i in range(1, n+1):
    dp[i] = dp[i-1].copy()
    for b in blocks[i-1]:
        for j in range(b, h+1):
            dp[i][j] += dp[i-1][j-b]

print(dp[n][h] % 10007)
# print(dp)

# https://howudong.tistory.com/106