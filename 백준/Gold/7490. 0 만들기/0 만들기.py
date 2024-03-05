import copy

symbols = [' ', '+', '-']

# c : 현재 숫자, s : 현재 합, b : 계산 형태, p : 프린트 형태, n : 목표 숫자
def zero_making(c, s, b, p, n):
    if c == n:
        if s == 0:
            print(''.join(map(str, p)))
        return
    for sym in symbols:
        new_b = copy.deepcopy(b)
        new_p = copy.deepcopy(p)
        new_p.append(sym)
        new_p.append(c + 1)
        if sym == ' ':
            if len(new_b) == 1:
                zero_making(c+1, s*10+c+1, [s*10+c+1], new_p, n)
            else:
                temp_n = new_b.pop()
                temp_s = new_b[-1]
                new_b.append(temp_n*10 + (c+1))
                if temp_s == '+':
                    zero_making(c+1, s+temp_n*9+c+1, new_b, new_p, n)
                elif temp_s == '-':
                    zero_making(c+1, s-(temp_n*9+c+1), new_b, new_p, n)
        elif sym == '+':
            new_b.append(sym)
            new_b.append(c + 1)
            zero_making(c+1, s+c+1, new_b, new_p, n)
        else:
            new_b.append(sym)
            new_b.append(c + 1)
            zero_making(c+1, s-c-1, new_b, new_p, n)

test = int(input())
for t in range(test):
    n = int(input())
    zero_making(1, 1, [1], [1], n)
    if t != test-1:
        print()