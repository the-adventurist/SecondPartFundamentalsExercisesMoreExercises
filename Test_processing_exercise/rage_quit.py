sequence_to_message = input()
result_string = ''
temp_string = ''
current_digit = ''
for current_symbol in range(len(sequence_to_message)):
    if sequence_to_message[current_symbol].isalpha():
        temp_string += sequence_to_message[current_symbol].upper()
    elif sequence_to_message[current_symbol].isdigit():
        current_digit += sequence_to_message[current_symbol]
        if current_symbol < len(sequence_to_message) -1 and sequence_to_message[current_symbol + 1].isdigit():
            continue
        current_digit_as_digit = int(current_digit)
        current_digit = ''
        temp_string *= current_digit_as_digit
        result_string += temp_string
        temp_string = ''
    else:
        temp_string += sequence_to_message[current_symbol]

unique_symbols = set(result_string)

print(f'Unique symbols used: {len(unique_symbols)}')
print(result_string)
