import re

furniture_purchases = []
total_price = 0

pattern = r'^>>([a-zA-Z]+)<<([0-9]+(?:\.[0-9]+)?)!([0-9]+)$'
re.escape(pattern)
data = input()
while data != 'Purchase':
    sorted_data = re.match(pattern, data)
    print(sorted_data)
    furniture = sorted_data.group(1)
    price = float(sorted_data.group(2))
    quantity = int(sorted_data.group(3))
    total_price += (price * quantity)
    furniture_purchases.append(furniture)
    data = input()
print('Bought furniture:')
print('\n'.join(furniture_purchases))
print(f'Total money spend: {total_price:.2f}')
