n = int(input())
blocks = [int(input()) for _ in range(n)]

step_one = list(map(int, input().split(' ')))
step_two = list(map(int, input().split(' ')))

def remove_blocks(blocks, block_range):
    start, end = block_range[0], block_range[1]
    temp_blocks = []
    for idx, block in enumerate(blocks):
        if idx >= start - 1 and idx <= end - 1:
            continue
        temp_blocks.append(block)
    return temp_blocks

step_one_blocks = remove_blocks(blocks, step_one)
step_two_blocks = remove_blocks(step_one_blocks, step_two)

print(len(step_two_blocks))
for block in step_two_blocks:
    print(block)