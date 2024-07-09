n, t = (int(num) for num in input().split())
up_conatiner = [int(num) for num in input().split()]
down_conatiner = [int(num) for num in input().split()]

for _ in range(t):
    up_temp_num = up_conatiner[-1]
    for i in range(n-1, 0, -1):
        up_conatiner[i] = up_conatiner[i-1]

    down_temp_num = down_conatiner[-1]
    for i in range(n-1, 0, -1):
        down_conatiner[i] = down_conatiner[i-1]

    up_conatiner[0] = down_temp_num
    down_conatiner[0] = up_temp_num

print(' '.join(list(map(str, up_conatiner))))
print(' '.join(list(map(str, down_conatiner))))