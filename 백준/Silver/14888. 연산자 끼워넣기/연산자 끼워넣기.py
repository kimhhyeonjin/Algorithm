N = int(input())
A = list(map(int, input().split()))
pl, mi, mu, di = list(map(int, input().split()))
minV = 10000000000
maxV = -1000000000

def dfs(i, val):
    global pl, mi, mu, di, minV, maxV
    if i == N:
        maxV = max(maxV, val)
        minV = min(minV, val)
    else:
        if pl > 0:
            pl -= 1
            dfs(i+1, val + A[i])
            pl += 1
        if mi > 0:
            mi -= 1
            dfs(i+1, val - A[i])
            mi += 1
        if mu > 0:
            mu -= 1
            dfs(i+1, val * A[i])
            mu += 1
        if di > 0:
            di -= 1
            if val >= 0:
                dfs(i+1, val // A[i])
            else:
                dfs(i+1, -((-val) // A[i]))
            di += 1

dfs(1, A[0])
print(maxV)
print(minV)