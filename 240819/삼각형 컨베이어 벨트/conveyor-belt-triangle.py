n, t = (int(num) for num in input().split())
containers = [[int(num) for num in input().split()] for _ in range(3)]

temp_num = 0

for _ in range(t):
    for container in containers:
        last_num = container[-1]
        for i in range(n-1, 0, -1):
            container[i] = container[i-1]

        container[0] = temp_num
        temp_num = last_num

    containers[0][0] = temp_num

for container in containers:
    print(' '.join(list(map(str, container))))