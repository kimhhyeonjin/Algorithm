N = int(input())
A = list(map(int, input().split()))
B, C = list(map(int, input().split()))

cnt = 0
for i in range(N):
    super = A[i]
    cnt += 1
    super -= B
    if super > 0:
        if super % C == 0:
            cnt += (super // C)
        else:
            cnt += ((super // C) + 1)
print(cnt)