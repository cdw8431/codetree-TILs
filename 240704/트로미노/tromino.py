from collections import deque

n, m = [int(num) for num in input().split()]
matrix = [[int(num) for num in input().split()] for _ in range(n)]

max_num = 0

for row in range(n):
    for col in range(m):
        if col + 2 >= m:
            break
        box_num = sum([matrix[row][col+i] for i in range(3)])
        if box_num > max_num:
            max_num = box_num

for col in range(m):
    for row in range(n):
        if row + 2 >= n:
            break
        box_num = sum([matrix[row+i][col] for i in range(3)])
        if box_num > max_num:
            max_num = box_num

for row in range(n):
    if row + 1 >= n:
        break
    for col in range(m):
        if col + 1 >= m:
            break
        box = deque([(0,0), (0,1), (1,1), (1,0)])
        box_nums = []
        for _ in range(4):
            box_nums.append(sum(matrix[row+box[i][0]][col+box[i][1]] for i in range(3)))
            box.append(box.popleft())

        max_box_num = max(box_nums)
        if max_box_num > max_num:
            max_num = max_box_num

print(max_num)