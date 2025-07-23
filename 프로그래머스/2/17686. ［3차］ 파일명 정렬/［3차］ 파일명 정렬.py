def solution(files):
    answer = []
    file_list = []
    
    for file in files:
        head = ''
        number = ''
        tail = ''
        for f in range(len(file)):
            if file[f].isdigit():
                number += file[f]
            else:
                if not number:
                    head += file[f]
                else:
                    tail += file[f:]
                    break
        file_list.append([head, number, tail])
    file_list.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    for f in file_list:
        answer.append(''.join(f))
    
    return answer