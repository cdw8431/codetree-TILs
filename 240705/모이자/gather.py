n = int(input())
houses = [int(num) for num in input().split()]

distances = []
for i in range(len(houses)):
    sum_distance = 0
    for j, house_person in enumerate(houses):
        distance = abs(i - j)
        if distance == 0:
            continue
        sum_distance += house_person * distance
    distances.append(sum_distance)

print(min(distances))