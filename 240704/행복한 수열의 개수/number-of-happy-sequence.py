n, m = (int(i) for i in input().split())

sequences = []
for i in range(n):
    sequences.append([int(num) for num in input().split()])

def get_happy_sequence_count(pivot) -> int:
    result = 0
    for i in range(n):
        nums = []
        for j in range(n):
            row = i if pivot == 'row' else j
            col = j if pivot == 'row' else i
            current_num = sequences[row][col]
            if not nums or nums and nums[-1] == current_num:
                nums.append(current_num)
            if len(nums) == m:
                result += 1
                break
    return result
    

happy_sequence_count = get_happy_sequence_count(pivot='row') + get_happy_sequence_count(pivot='col')
print(happy_sequence_count)