chars = input()
length = len(chars)

case_count = 0
for idx, char in enumerate(chars):
    if char != '(' or idx >= length:
        continue
    for char in chars[idx+1:]:
        if char == ')':
            case_count += 1

print(case_count)