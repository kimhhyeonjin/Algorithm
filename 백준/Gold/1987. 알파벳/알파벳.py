def dfs(horse, cnt):
    global res
    i, j = horse[0], horse[1]
    res = max(res, cnt)
    for di, dj in d:
        if 0 <= i + di < R and 0 <= j + dj < C and board[i+di][j+dj] not in alphabet:
            alphabet.add(board[i+di][j+dj])
            dfs([i+di, j+dj], cnt+1)
            alphabet.remove(board[i+di][j+dj])

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
alphabet = set()
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

horse = [0, 0]
alphabet.add(board[0][0])

# dfs
res = 0
# visited는 alphabet과 같은 역할을 하기 때문에 필요 없음
dfs(horse, 1)
print(res)