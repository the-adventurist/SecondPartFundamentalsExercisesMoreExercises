import re

furniture_purchases = []
total_price = 0

pattern = r'>>([a-zA-Z]+)<<(\d+(\.\d+)?)!(\d+)'
data = input()
while data != 'Purchase':
    sorted_data = re.finditer(pattern, data)
    for current_group in sorted_data:
        if current_group.group(2) != '0' or current_group.group(4) != 0:
            furniture_purchases.append(current_group.group(1))
            current_total_price = float(current_group.group(2)) * int(current_group.group(4))
        else:
            current_total_price = 0
        total_price += current_total_price
    data = input()
print('Bought furniture:')
print('\n'.join(furniture_purchases))
print(f'Total money spend: {total_price:.2f}')
