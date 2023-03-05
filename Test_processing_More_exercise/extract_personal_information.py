number_of_lines = int(input())
name = ''
age = ''

for _ in range(number_of_lines):
    current_line = input()
    index = current_line.find("@")
    index2 = current_line.find('|')
    index3 = current_line.find('#')
    index4 = current_line.find('*')
    name = current_line[index + 1: index2]
    age = current_line[index3 + 1: index4]
    print(f"{name} is {age} years old.")
