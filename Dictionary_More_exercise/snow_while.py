dwarfs = {}

data = input()
while data != "Once upon a time":
    name, hat_color, physics = data.split(' <:> ')
    physics = int(physics)
    if hat_color not in dwarfs:
        dwarfs[hat_color] = {}
    if name not in dwarfs[hat_color]:
        dwarfs[hat_color][name] = physics
    if name in dwarfs[hat_color]:
        for current_hat, additional_info in dwarfs.items():
            for current_name, current_physics in additional_info.items():
                if current_physics < physics:
                    dwarfs[hat_color][name] = physics
    data = input()

sorted_dwarfs = sorted()

print(sorted_dwarfs)
print(dwarfs)