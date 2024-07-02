n = int(input())
size = 3

box = []
for _ in range(n):
    box.append([int(i) for i in input().split()])

def get_area_number(row_s, row_e, col_s, col_e):
    area_num = 0
    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            if box[row][col]:
                area_num += 1
    return area_num

max_num = 0
for row in range(n):
    row_e = (row + size) - 1
    if row_e >= n:
        break

    for col in range(n):
        col_e = (col + size) - 1
        if col_e >= n:
            break

        area_num = get_area_number(row, row_e, col, col_e)
        if area_num > max_num:
            max_num = area_num
    
print(max_num)