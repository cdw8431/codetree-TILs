n, m, q = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]

tasks = [input().split() for _ in range(q)]

def wind(matrix: list[list[int]], inner_r: int, is_left: bool):
    row_num = inner_r - 1
    row = matrix[row_num]

    if is_left:
        matrix[row_num] = [row[-1], *row[0:-1]]
    else:
        matrix[row_num] = [*row[1:], row[0]]

    is_first = r == inner_r
    if not is_first and (row_num == 0 or row_num == n-1):
        return

    row = matrix[row_num]
    next_direction = not is_left

    # 위로 전파되는 바람
    can_upward = row_num > 0 and any(current_e == next_e for current_e, next_e in zip(row, matrix[row_num-1]))
    if r > inner_r and can_upward:
        wind(matrix, inner_r - 1, next_direction)

    # 아래로 전파되는 바람
    can_downward = row_num < n-1 and any(current_e == next_e for current_e, next_e in zip(row, matrix[row_num+1]))
    if r < inner_r and can_downward:
        wind(matrix, inner_r + 1, next_direction)

    # 첫 바람
    if is_first:
        if can_upward:
            wind(matrix, inner_r - 1, next_direction)
        if can_downward:
            wind(matrix, inner_r + 1, next_direction)

for task in tasks:
    r, d = int(task[0]), task[1]
    wind(matrix, r, d == 'L')

for row in matrix:
    print(' '.join(list(map(str, row))))