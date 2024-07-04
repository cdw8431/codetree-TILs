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
        box_pattern = [(0,0), (0,1), (1,1), (1,0)]
        box_nums = []
        for _ in range(4):
            box_num = sum([matrix[row+idx[0]][col+idx[1]] for idx in box_pattern[:3]])
            box_nums.append(box_num)
            box_pattern = [box_pattern[-1], *box_pattern[:3]]

        if max(box_nums) > max_num:
            max_num = box_num

print(max_num)