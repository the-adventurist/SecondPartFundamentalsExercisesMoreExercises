phonebook = {}

info = input()
while not info.isdigit():
    name, phone_number = info.split('-')
    phonebook[name] = phone_number
    info = input()
for _ in range(int(info)):
    searched_name = input()
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
