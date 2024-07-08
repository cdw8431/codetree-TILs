n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

max_coin = 0

for row in range(n):
    for col in range(n):
        if col + 2 >= n:
            break
        temp_max_coin = sum([matrix[row][i] for i in range(col, col + 3)])
        if temp_max_coin > max_coin:
            max_coin = temp_max_coin
        
print(max_coin)