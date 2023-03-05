sequence_letters_numbers = input().split()
results = []

for current_group in sequence_letters_numbers:
    first_letter = current_group[0]
    second_letter = current_group[-1]
    number = int(current_group[1:-1])
    temp_result = 0
    if first_letter.isupper():
        temp_result = number / (ord(first_letter) - 64)
    else:
        temp_result = number * (ord(first_letter) - 96)
    if second_letter.isupper():
        temp_result = temp_result - (ord(second_letter) - 64)
    else:
        temp_result = (ord(second_letter) - 96) + temp_result
    results.append(temp_result)

print(f'{sum(results):.2f}')
