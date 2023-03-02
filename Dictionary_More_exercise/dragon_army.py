def dragons_filler(current_type, dragon_name, dragons_damage, dragons_health, dragons_armor):
    dragons_damage = int(dragons_damage)
    dragons_health = int(dragons_health)
    dragons_armor = int(dragons_armor)
    dragons_by_names[dragon_name] = {'types_dragon': current_type,'damage': dragons_damage,
                                     'health': dragons_health, 'armor': dragons_armor}


dragons_by_names = {}
type_dragons_avg_info = {}

number_of_dragons = int(input())
for _ in range(number_of_dragons):
    type_, name, damage, health, armor = input().split()
    if damage == 'null':
        damage = 45
    if health == 'null':
        health = 250
    if armor == 'null':
        armor = 10
    dragons_filler(type_, name, damage, health, armor)

list_of_types = []
for info in dragons_by_names.values():
    if info['types_dragon'] not in list_of_types:
        list_of_types.append(info['types_dragon'])

print(list_of_types)
filtered_info_by_type = {}
for present_type in list_of_types:
    filtered_info_by_type[present_type] = {'avr_damage': 0, 'avr_health': 0, 'avr_armor': 0}
    sum_damage = 0
    sum_health = 0
    sum_armor = 0
    occurrence = 0
    for info in dragons_by_names.values():
        if present_type == info.get('types_dragon'):
            sum_damage += info['damage']
            occurrence += 1
            sum_health += info['health']
            sum_armor += info['armor']
    if sum_damage:
        avr_damage = sum_damage / occurrence
        avr_health = sum_health / occurrence
        avr_armor = sum_armor / occurrence
        filtered_info_by_type[present_type]['avr_damage'] += avr_damage
        filtered_info_by_type[present_type]['avr_health'] += avr_health
        filtered_info_by_type[present_type]['avr_armor'] += avr_armor
        type_dragons_avg_info.update(filtered_info_by_type)



sorted_dragons_by_names = sorted(dragons_by_names.items(), key=lambda x: x[0])
print(sorted_dragons_by_names)
for current_type, data in type_dragons_avg_info.items():
    for _ in data.items():
        print(f"{current_type}::({data['avr_damage']:.2f}/{data['avr_health']:.2f}/{data['avr_armor']:.2f})")
        for name, data_details in sorted_dragons_by_names:
            print(f"-{name} -> damage: {data_details['damage']}, health: {data_details['health']}, "
                  f"armor: {data_details['armor']}")