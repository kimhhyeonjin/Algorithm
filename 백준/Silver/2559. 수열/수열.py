N, K = list(map(int, input().split()))
temp = list(map(int, input().split()))

t_sum = sum(temp[:K])
t_max = sum(temp[:K])
for i in range(N - K):
    t_sum = t_sum - temp[i] + temp[i + K]
    if t_sum > t_max:
        t_max = t_sum
print(t_max)