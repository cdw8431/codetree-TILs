n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

max_num = 0

def get_inclined_rectangle_sum(row, col):
    rectangle_sum = 0

    for rec_col in range(col, n):
        rec_row = row-rec_col+1
        rectangle_sum += matrix[rec_row][rec_col] + matrix[rec_row-1][rec_col-1]
        if rec_row - 1 == 0:
            break

    return rectangle_sum


for row in range(2, n):
    for col in range(1, n):
        temp_max_num = get_inclined_rectangle_sum(row, col)
        if temp_max_num > max_num:
            max_num = temp_max_num

print(max_num)