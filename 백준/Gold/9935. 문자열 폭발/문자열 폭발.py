word = input()
bomb = input()
l = len(bomb)

# while문으로 남은 문자열을 폭발이 일어나지 않을 때까지
# 반복해서 돌리는 것이 아니고
# stack에 문자를 하나씩 추가하면서 폭발이 일어나는 경우 제거하고
# 새로 생긴 문자열의 폭발도 바로 확인
stack = []
for i in word:
    stack.append(i)
    if ''.join(stack[-l:]) == bomb:
        for _ in range(l):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')