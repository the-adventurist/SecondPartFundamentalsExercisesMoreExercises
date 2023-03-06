keys = [int(x) for x in input().split()]
line = input()
while line != 'find':
    encrypt_message = ''
    index = 0
    for symbol in line:
        new_symbol = chr(ord(symbol) - keys[index])
        encrypt_message += new_symbol
        index += 1
        if index == len(keys):
            index = 0
    start_index = encrypt_message.find('&') + 1
    encrypt_message = encrypt_message.replace('&', '|', 1)
    end_index = encrypt_message.find('&')
    name = encrypt_message[start_index: end_index]
    start_i_coord = encrypt_message.find('<') + 1
    end_i_coord = encrypt_message.find('>')
    coordinates = encrypt_message[start_i_coord: end_i_coord]
    print(f"Found {name} at {coordinates}")
    line = input()
