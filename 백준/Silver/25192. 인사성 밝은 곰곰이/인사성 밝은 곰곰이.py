N = int(input())
nick = set()
cnt = 0
for i in range(N):
    chat = input()
    if chat == "ENTER":
        cnt += len(nick)
        nick = set()
    else:
        if chat not in nick:
            nick.add(chat)
else:
    cnt += len(nick)
print(cnt)