import math

products_dict = {}

while True:
    command = input().split()
    if command[0] == "buy":
        break

    name = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if name not in products_dict.keys():
        products_dict[name] = [price, quantity]
    else:
        products_dict[name][0] = price
        products_dict[name][1] += quantity

for key, value in products_dict.items():
    value = math.prod(value)
    print(f"{key} -> {value:.2f}")