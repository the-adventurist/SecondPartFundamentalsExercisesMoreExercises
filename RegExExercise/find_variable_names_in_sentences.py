import re

sentence = input()
pattern = r'(?<!_)_([a-zA-Z0-9]+)(?=\s|(?=$))'

word_extraction = re.finditer(pattern, sentence)
print_string = ''
for word in word_extraction:
    print_string += word.group(1) + ','
print(print_string.rstrip(','))
