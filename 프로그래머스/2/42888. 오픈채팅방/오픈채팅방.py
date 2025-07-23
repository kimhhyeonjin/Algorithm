def solution(record):
    answer = []
    code_info = {"Enter" : "님이 들어왔습니다.", "Leave" : "님이 나갔습니다."}
    nickname_info = {}
    
    for r in record:
        if r[0] != "L":
            c, i, n = r.split()
            nickname_info[i] = n
    
    for r in record:
        if r[0] == "L":
            c, i = r.split()
            answer.append(nickname_info[i] + code_info[c])
        else:
            c, i, n = r.split()
            if c == "Enter":
                answer.append(nickname_info[i] + code_info[c])
    
    return answer