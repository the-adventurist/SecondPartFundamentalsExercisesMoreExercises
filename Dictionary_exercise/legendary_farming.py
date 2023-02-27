materials_dictionary = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_dictionary = {}

collect_legendary_item = False
while True:
    delivery_details = input().lower().split()
    for i in range(0, len(delivery_details), 2):
        element = delivery_details[i + 1]
        qty = int(delivery_details[i])
        if element in materials_dictionary:
            materials_dictionary[element] += qty
        if materials_dictionary['shards'] >= 250:
            materials_dictionary['shards'] -= 250
            print('Shato')
            if element == 'shards':
                legendary_item = 'Shatowmourne'
            elif element == 'fragments':
                legendary_item = 'Valanyr'
            elif element == 'motes':
                legendary_item = 'Dragonwrath'
            print(f'{legendary_item} obtained!')
            collect_legendary_item = True
            break
        else:
            junk_dictionary[element] = junk_dictionary.get(element, 0) + qty
    if collect_legendary_item:
        break

print(f'shards: {materials_dictionary["shards"]}')
print(f'fragments: {materials_dictionary["fragments"]}')
print(f'motes: {materials_dictionary["motes"]}')

for element, qty in junk_dictionary.items():
    print(f'{element}: {qty}')
