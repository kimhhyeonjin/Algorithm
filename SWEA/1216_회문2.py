import sys
sys.stdin = open('1216_회문2.txt')

for tc in range(1, 11):
    num = input()
    string = []
    for _ in range(100):
        string.append(input())
    # print(string)  # ['', '', '', '', ...]의 형태

    max_length = 0

    # 가로
    for i in range(100):
        for j in range(100):
            length = 0
            for k in range(100-j+1):  # range에 +1
            # 슬라이싱도 range처럼 [a:b]인 경우 a부터 b-1까지 실행
                if string[i][j:j+k] == string[i][j:j+k][::-1]:
                    # length = len(string[i][j:j+k])
                    length = k
                if max_length < length:
                    max_length = length

    # 세로
    for i in range(100):
        for j in range(100):
            length = 0
            text = ''  # 초기화 위치 제발
            for k in range(100-j):
                text += string[j+k][i]
                if text == text[::-1]:
                    length = len(text)
                if max_length < length:
                    max_length = length

    print(f'#{tc} {max_length}')