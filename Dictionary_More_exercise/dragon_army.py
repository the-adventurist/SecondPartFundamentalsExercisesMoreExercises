dragons = {}
types_avg_stats = {}

numbers_of_dragons = int(input())
for _ in range(numbers_of_dragons):
    type_, name, damage, health, armor = input().split()
    if damage == 'null':
        damage = 45
    else:
        damage = int(damage)
    if health == 'null':
        health = 250
    else:
        health = int(health)
    if armor == 'null':
        armor = 10
    else:
        armor = int(armor)
    if type_ not in dragons:
        dragons[type_] = {}
        types_avg_stats[type_] = [0, 0, 0, 0]
    if name not in dragons[type_]:
        dragons[type_][name] = {'damage': damage, 'health': health, 'armor': armor}
        types_avg_stats[type_][0] += damage
        types_avg_stats[type_][1] += health
        types_avg_stats[type_][2] += armor
        types_avg_stats[type_][3] += 1
    else:
        types_avg_stats[type_][0] -= dragons[type_][name]['damage']
        types_avg_stats[type_][1] -= dragons[type_][name]['health']
        types_avg_stats[type_][2] -= dragons[type_][name]['armor']
        dragons[type_][name] = {'damage': damage, 'health': health, 'armor': armor}
        types_avg_stats[type_][0] += damage
        types_avg_stats[type_][1] += health
        types_avg_stats[type_][2] += armor

for current_type, values in types_avg_stats.items():
    new_values = []
    for current_value in range(len(values) - 1):
        if values[current_value] != 0 and values[-1] != 0:
            new_value = values[current_value] / values[-1]
            new_values.append(new_value)
        else:
            new_values.append(0)
    types_avg_stats[current_type] = new_values

for type_, data in dragons.items():
    print(f"{type_}::({types_avg_stats[type_][0]:.2f}/{types_avg_stats[type_][1]:.2f}/{types_avg_stats[type_][2]:.2f})")
    sorted_data = sorted(data.items(), key=lambda x: x[0])
    for name, details in sorted_data:
        print(f"-{name} -> damage: {details['damage']}, health: {details['health']}, armor: {details['armor']}")

