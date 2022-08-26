height = []
for _ in range(9):
    height.append(int(input()))
# print(height)

# 버블소트
for i in range(8, 0, -1):
    for j in range(i):
        if height[j] > height[j+1]:
            height[j], height[j+1] = height[j+1], height[j]

flag = 1
for i in range(9):
    for j in range(9):
        if i < j and (sum(height)-height[i]-height[j]) == 100:
            for num in range(9):
                if num not in [i, j]:
                    print(height[num])
            flag = 0
            break
    if flag == 0:
        break

######################################################################
# 틀린 제출
'''
height = []
for _ in range(9):
    height.append(int(input()))
# print(height)

# 버블소트
for i in range(8, 0, -1):
    for j in range(i):
        if height[j] > height[j+1]:
            height[j], height[j+1] = height[j+1], height[j]

while True:
    for i in range(9):
        for j in range(9):
            if i < j and (sum(height)-height[i]-height[j]) == 100:
                for num in range(9):
                    if num not in [i, j]:
                        print(height[num])
                        break
                        
반례
1
9
2
8
3
7
4
6
70
'''