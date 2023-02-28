force_book = {}

info = input()
while info != "Lumpawaroo":
    info_details = info.split(' | ')
    exists_such_force_user = False
    if len(info_details) > 1:
        force_side, force_user = info_details
        for current_side, users in force_book.items():
            for current_user in users:
                if current_user == force_user:
                    exists_such_force_user = True
                    break
            if exists_such_force_user:
                break
        if exists_such_force_user:
            info = input()
            continue
        if force_side not in force_book:
            force_book[force_side] = []
        force_book[force_side].append(force_user)
    else:
        force_user, force_side = info.split(' -> ')
        for current_side, users in force_book.items():
            for current_user in users:
                if current_user == force_user:
                    exists_such_force_user = True
                    force_book[current_side].remove(force_user)
                    break
            if exists_such_force_user:
                break
        if force_side not in force_book:
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    info = input()

for current_side, users in force_book.items():
    if len(users) > 0:
        print(f'Side: {current_side}, Members: {len(users)}')
        for user in users:
            print(f'! {user}')
