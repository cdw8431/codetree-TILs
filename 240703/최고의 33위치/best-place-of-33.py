n = int(input())

box = []
for _ in range(n):
    box.append([int(i) for i in input().split()])

max_num = 0
for idx in range(n - 3) or [0]:
    sum_num = 0
    for row in range(n):
        for col in range(n):
            if box[row + idx][col + idx]:
                sum_num += 1
    if sum_num > max_num:
        max_num = sum_num

print(max_num)