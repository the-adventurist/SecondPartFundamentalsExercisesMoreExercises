import re

pattern = r'%([A-Z]{1}[a-z]+)%.*?<(\w+)>.*?\|(\d+)\|.*?(\d+(?:[\.\d]*)(?=\$))'

total_income = 0
data_info = input()
while data_info != 'end of shift':
    extract_data = re.finditer(pattern, data_info)
    for current_element in extract_data:
        customer = current_element.group(1)
        product = current_element.group(2)
        quantity = int(current_element.group(3))
        price = float(current_element.group(4))
        total_purchase = quantity * price
        total_income += total_purchase
        print(f"{customer}: {product} - {total_purchase:.2f}")
    data_info = input()
print(f"Total income: {total_income:.2f}")
