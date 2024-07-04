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
        max_box_num = max([
            matrix[row+0][col+0] + matrix[row+0][col+1] + matrix[row+1][col+1],
            matrix[row+0][col+1] + matrix[row+1][col+1] + matrix[row+1][col+0],
            matrix[row+1][col+1] + matrix[row+1][col+0] + matrix[row+0][col+0],
            matrix[row+1][col+0] + matrix[row+0][col+0] + matrix[row+0][col+1]
        ])
        if max_box_num >= max_num:
            max_num = max_box_num

print(max_num)