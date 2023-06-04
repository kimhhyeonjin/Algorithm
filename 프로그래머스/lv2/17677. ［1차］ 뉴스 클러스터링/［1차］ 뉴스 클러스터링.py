def solution(str1, str2):
    answer = 0
    
    # 소문자로 변환 후 비교
    str1_n = str1.lower()
    str2_n = str2.lower()
    
    # 두 글자씩 끊기
    temp_in = {}
    temp_un = {}
    inter = {}
    union = {}
    
    # 첫번째 문자열부터 계산
    for i in range(len(str1_n)-1):
        str = str1_n[i:i+2]
        # 영문자인 경우만 추가
        if str.isalpha():
            if str in temp_in:
                temp_in[str] += 1
            else:
                temp_in[str] = 1
            if str in temp_un:
                temp_un[str] += 1
            else:
                temp_un[str] = 1

    # 두번째 문자열 계산
    for i in range(len(str2_n)-1):
        str = str2_n[i:i+2]
        # 영문자인 경우
        if str.isalpha():
            # temp_in에 해당 str이 있으면
            # temp_in에서 1만큼 줄이고 inter에 추가
            # 이 때 temp_in 값이 0이면 temp_in 삭제
            if str in temp_in:
                if str in inter:
                    inter[str] += 1
                else:
                    inter[str] = 1
                temp_in[str] -= 1
                if temp_in[str] == 0:
                    del temp_in[str]
            # union에는 항상 추가
            if str in union:
                union[str] += 1
            else:
                union[str] = 1
                
    # temp_un과 union 합집합 구하기
    for i in temp_un:
        # union에 없는 경우 더하기
        if i not in union:
            union[i] = temp_un[i]
        # union에 있는 경우 값 비교 후 큰 값 선택
        else:
            if temp_un[i] > union[i]:
                union[i] = temp_un[i]
                
    # inter와 union value 개수 구하기
    a = 0
    b = 0
    for i in inter:
        a += inter[i]
    for j in union:
        b += union[j]

    # answer 값
    if len(inter) == 0 and len(union) == 0:
        answer = 65536
    else:
        answer = int(a / b * 65536)
    
    return answer