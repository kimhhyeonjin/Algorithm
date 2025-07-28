def solution(m, n, board):
    answer = 0
    board_list = list(list(b) for b in board)
    
    flag = True
    d = [[0, 0], [1, 0], [0, 1], [1, 1]]
    while flag:
        flag = False
        check_list = [[0] * n for _ in range(m)]
        for i in range(m - 1):
            for j in range(n - 1):
                temp = board_list[i][j]
                if temp == '':
                    continue
                for di, dj in d:
                    if temp != board_list[i + di][j + dj]:
                        break
                else:
                    flag = True
                    for di, dj in d:
                        check_list[i + di][j + dj] = 1
        
        if flag:
            for i in range(m):
                for j in range(n):
                    if check_list[i][j]:
                        answer += 1
                        board_list[i][j] = ''
    
            for j in range(n):
                block = []
                for i in range(m):
                    if board_list[i][j] != '':
                        block.append(board_list[i][j])
                block = [''] * (m - len(block)) + block
                for i in range(m):
                    board_list[i][j] = block[i]
                
    return answer