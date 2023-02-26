mine = {}

while True:
    input_ = input()
    if input_ == 'stop':
        break
    resource_ = input_
    input_ = input()
    qty = int(input_)
    mine[resource_] = mine.get(resource_, 0) + qty

for this_resource, its_quantity in mine.items():
    print(f'{this_resource} -> {its_quantity}')
