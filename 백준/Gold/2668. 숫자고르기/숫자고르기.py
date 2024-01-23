def dfs(num):
    a.add(num)
    b.add(nums[num])
    # 사이클이 만들어진 경우
    if nums[num] in a:
        # 완전한 사이클
        if a == b:
            ans.extend(list(a))
        # 불완전한 사이클
        return
    dfs(nums[num])

N = int(input())
nums = [[] for _ in range(N+1)]
ans = []
for i in range(1, N+1):
    num = int(input())
    nums[i] = num
    if i == num:
        ans.append(num)

for i in range(1, N+1):
    if i not in ans:
        a = set()
        b = set()
        dfs(i)

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])