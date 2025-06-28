# def solution(phone_book):
#     answer = True
    
#     # hash 이용하기
#     phone = {}
#     for i in phone_book:
#         phone[i] = i
#     # print(phone)
    
#     for i in phone_book:
#         temp = ''
#         for j in i:
#             temp += j
#             if temp in phone and temp != i:
#                 answer = False
#     return answer

def solution(phone_book):
    
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True