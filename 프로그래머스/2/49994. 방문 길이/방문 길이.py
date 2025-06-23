def solution(dirs):
    d = {'U': [-1, 0, 'D'], 'D': [1, 0, 'U'], 'R': [0, 1, 'L'], 'L': [0, -1, 'R']}
    arr = [[[] for _ in range(11)] for _ in range(11)]
    answer = 0
    
    cur = [5, 5]
    for direction in dirs:
        di, dj, nd = d[direction]
        ni, nj = cur[0] + di, cur[1] + dj
        if 0 <= ni < 11 and 0 <= nj < 11:
            # 좌표 평면 내에 있으면
            if nd in arr[ni][nj]:
                # 횟수는 세지 않고 현재 위치 바꾸기
                cur = [ni, nj]
                
            else:
                # 횟수도 세고 현재 위치도 바꾸고 nd 추가
                answer += 1
                arr[cur[0]][cur[1]].append(direction)
                cur = [ni, nj]
                arr[ni][nj].append(nd)
            
    return answer