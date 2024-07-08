n = int(input())
cow_heights = [int(num) for num in input().split()]

match_count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cow_heights[i] < cow_heights[j] < cow_heights[k]:
                match_count += 1

print(match_count)