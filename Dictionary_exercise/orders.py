stock = {}

product_data = input()
while product_data != 'buy':
    product, price, qty = product_data.split()
    price = float(price)
    qty = int(qty)
    if product not in stock:
        stock[product] = [price]
    stock[product][0] = price
    if len(stock[product]) == 1:
        stock[product].append(0)
    stock[product][1] += qty
    product_data = input()

for product, product_price_qty in stock.items():
    total_price = product_price_qty[0] * product_price_qty[1]
    print(f'{product} -> {total_price:.2f}')
