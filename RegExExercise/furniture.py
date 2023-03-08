import re

furniture_purchases = []
total_price = 0

pattern = r'^\>\>([a-zA-Z]+)\<\<(\d+(?:[\.\d]*))\!(\d+)$'
re.escape(pattern)
data = input()
while data != 'Purchase':
    sorted_data = re.finditer(pattern, data)
    for details in sorted_data:
        furniture_purchases.append(details.group(1))
        total_price += (float(details.group(2)) * int(details.group(3)))
    data = input()
print('Bought furniture:')
print('\n'.join(furniture_purchases))
print(f'Total money spend: {total_price:.2f}')
