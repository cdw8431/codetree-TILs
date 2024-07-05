n, m = [int(num) for num in input().split()]
matrix = [[int(num) for num in input().split()] for _ in range(n)]

max_k = 2 * (n - 1) + 1

def mining_gold(row, col, k):
    gold = 0
    for i in range(n):
        for j in range(n):
           if abs(row - i) + abs(col - j) <= k and matrix[i][j] == 1:
                gold += 1
    return gold

max_gold = 0

for row in range(n):
    for col in range(n):
        for k in range(max_k):
            gold = mining_gold(row, col, k)

            pay = k * k + (k + 1) * (k + 1)
            gold_price = gold * m

            if pay <= gold_price and gold > max_gold:
                max_gold = gold

print(max_gold)