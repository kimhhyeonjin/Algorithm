num = int(input())
order = list(map(int, input().split()))
line = []

for i in range(num):
    line.insert(order[i], i+1)

print(*line[::-1])
# 순서대로 나열하고 마지막에 [::-1]을 이용하면 간단