import sys
sys.stdin = open('1221_GNS.txt')

def pre_process(pattern):
    lps = [0] * len(pattern)
    j = 0  # lps를 만들기 위한 prefix index

    for i in range(1, len(pattern)):  # 0번째 자리는 패턴 확인할 필요없음
        # prefix index 위치에 있는 문자와 비교
        if pattern[i] == pattern[j]:
            lps[i] = j + 1  # i의 앞에 중복되는 패턴이 존재한다
            j += 1  # j는 중복된 글자의 자리수
        else:
            j = 0
            # j = 0으로 이동 후 다음 prefix idx 비교를 한 번 더 해야 함
            if pattern[i] == pattern[j]:
                lps[i] = j + 1
                j += 1
    return lps

def KMP(text, pattern):
    lps = pre_process(pattern)  # 전처리로 lps 테이블 생성

    i = 0  # text index
    j = 0  # pattern index
    count = 0
    while i < len(text) and j < len(pattern):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == len(pattern):  # pattern이 전부 일치할 때
            count += 1
            j = 0  # j 초기화
    if count >= 1:
        return count
    else:
        return 0

T = int(input())  # 테스트 케이스 개수

num = ['ZRO ', 'ONE ', "TWO ", 'THR ', 'FOR ', 'FIV ', 'SIX ', 'SVN ', 'EGT ', 'NIN ']
for _ in range(T):
    tc, length = input().split()
    text = input() + ' '
    str_sorted = ''
    for pattern in num:
        count = KMP(text, pattern)
        str_sorted = str_sorted + pattern * count
    print(f'{tc}')
    print(str_sorted)