import re

pattern = r'.*?@([A-Za-z]+).*?:(\d+).*?!(A|D)!.*?->(\d+).*?'
key_letters = ['s', 't', 'a', 'r']
number_of_messages = int(input())
decrypted_messages = []
for _ in range(number_of_messages):
    current_key = 0
    encrypted_message = input()
    for current_letter in encrypted_message:
        if current_letter.lower() in key_letters:
            current_key += 1
    decrypted_message = ''
    for symbol in encrypted_message:
        decrypted_message += chr(ord(symbol) - current_key)
    decrypted_messages.append(decrypted_message)

attacked_planets = []
destroyed_planets = []
for decrypted_message in decrypted_messages:
    data = re.finditer(pattern, decrypted_message)
    for elements in data:
        planet_name = elements.group(1)
        if elements.group(3) == 'A':
            attacked_planets.append(planet_name)
        else:
            destroyed_planets.append(planet_name)

sorted_attacked_planets = sorted(attacked_planets)
print(f"Attacked planets: {len(sorted_attacked_planets)}")
for planet in sorted_attacked_planets:
    if attacked_planets:
        print(f"-> {planet}")

sorted_destroyed_planets = sorted(destroyed_planets)
print(f"Destroyed planets: {len(sorted_destroyed_planets)}")
for planet in sorted_destroyed_planets:
    if destroyed_planets:
        print(f"-> {planet}")
