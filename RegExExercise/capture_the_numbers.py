import re

data = input()
while data:
    pattern = r'[0-9]+'

    numbers = re.findall(pattern, data)
    if numbers:
        print(' '.join(numbers), end=' ')
    data = input()
