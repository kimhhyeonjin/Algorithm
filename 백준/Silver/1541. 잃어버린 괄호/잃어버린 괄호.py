str = input()

if '-' in str:
    new_str = str.split('-')
else:
    new_str = []
    new_str.append(str)
# print(new_str)
for ele in range(len(new_str)):
    if '+' not in new_str[ele]:
        new_str[ele] = '+' + new_str[ele]
    new_str[ele] = new_str[ele].split('+')
    total = 0
    for el in range(len(new_str[ele])):
        if new_str[ele][el] != '':
            total += int(new_str[ele][el])
    new_str[ele] = total
# print(new_str)
answer = new_str[0]
if len(new_str) > 1:
    for ele in range(1, len(new_str)):
        answer -= new_str[ele]

print(answer)
