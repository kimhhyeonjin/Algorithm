# 참고 https://westmino.tistory.com/82

chk = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
]

def tic_tac_toe(result, word):
    for c1, c2, c3 in chk:
        if result[c1] == result[c2] == result[c3] == word:
            return True
    else:
        return False

while True:
    t = input()
    if t == 'end':
        break
    # 반드시 첫 번째 사람이 X를 놓고 두 번째 사람이 O
    # X가 이기거나 비긴 경우 X의 개수가 O보다 1개 많고 O가 이긴 경우 X의 개수와 O의 개수가 같음
    x_count = t.count('X')
    o_count = t.count('O')
    if x_count == o_count or x_count == o_count + 1:
        # 승자가 있는지 확인 (승자가 있다면 패자 또한 있고 승자가 없다면 비김)
        t1, t2 = ['X', 'O'] if x_count == o_count + 1 else ['O', 'X']
        r1 = tic_tac_toe(t, t1)    # 이긴 팀
        r2 = tic_tac_toe(t, t2)    # 진 팀
        # 패자가 이기면 안됨
        if r2:
            print('invalid')
        # 승자가 지는 경우
        elif not r1:
            # 게임판이 가득 찬 경우 가능
            if t.count('.') == 0:
                print('valid')
            # 게임판이 가득 차지 않았는데 틱택토 성공한 사람이 없으므로 불가능
            else:
                print('invalid')
        # 승자가 이기고 패자가 진 경우
        else:
            print('valid')
    else:
        print('invalid')