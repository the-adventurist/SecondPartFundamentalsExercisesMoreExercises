this_string = input()
dict_signs_string = {}

for letter in this_string:
    if letter != ' ':
        dict_signs_string[letter] = dict_signs_string.get(letter, 0) + 1
for letter, its_count in dict_signs_string.items():
    print(f'{letter} -> {its_count}')
