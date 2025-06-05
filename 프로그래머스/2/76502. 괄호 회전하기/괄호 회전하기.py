def chk_pair(ss):
    stack = []
    pair = [['(', ')'], ['[', ']'], ['{', '}']]
    for i in range(len(ss)):
        if ss[i] in ('(', '[', '{'):
            stack.append(ss[i])
        else:
            for j in pair:
                if not stack:
                    return False
                if stack[-1] == j[0]:
                    if ss[i] == j[1]:
                        stack.pop()
                        break
                    else:
                        return False
    else:
        if stack:
            return False
    return True

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        new_s = s[i:] + s[:i]
        if chk_pair(new_s):
            answer += 1
    return answer