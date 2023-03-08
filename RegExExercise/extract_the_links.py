import re

pattern = r'www\.[a-zA-Z0-9-]+\.[a-z]+[\.a-z]*'
line = input()
while line:
    valid_links = re.findall(pattern, line)
    if valid_links:
        print(''.join(valid_links))
    line = input()
