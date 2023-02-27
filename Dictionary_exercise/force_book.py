force_book = {}

info = input()
while info != 'Lumpawaroo':
    info_details = info.split(' | ')
    if len(info_details) > 1:
        force_side, force_user = info_details
        if force_side not in force_book:
            force_book[force_side] = []
        current_user_not_present = False
        for force_side in force_book.values():
            if force_user in force_side:
                current_user_not_present = True
                info = input()
                continue
        force_book[force_side].append(force_user)
    else:
        info_details = info.split(' -> ')
        force_user, force_side = info_details
        if force_side in force_book:
            for side, users in force_book.items():
                for user in users:
                    if user == force_user:
                        force_book[side].remove(user)
                        break
            force_book[force_side].append(force_user)
        else:
            force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    info = input()

for side, users in force_book.items():
    if len(users) > 0:
        print(f'Side: {side}, Members: {len(users)}')
        for user in users:
            print(f'! {user}')
