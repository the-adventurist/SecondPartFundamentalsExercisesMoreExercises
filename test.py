strings = input()
default = 0
occurrences = dict.fromkeys(strings, default)
for letter in strings:
    occurrences[letter] += 1
del occurrences[' ']
for letter, count in occurrences.items():
    print(f"{letter} -> {count}")
