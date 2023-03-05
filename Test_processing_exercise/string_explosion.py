string = input()
left_power = 0

for current_symbol in range(len(string)):
    if string[current_symbol] == '>':
        if int(string[current_symbol + 1]) > 1:
            left_power += int(string[current_symbol + 1]) - 1
        string = string[:current_symbol + 1] + '*' + string[current_symbol + 2:]
    elif left_power and string[current_symbol] != '>' and string[current_symbol] != '*':
        string = string[:current_symbol] + '*' + string[current_symbol + 1:]
        left_power -= 1
string = [x for x in string if x != '*']
print(''.join(string))
