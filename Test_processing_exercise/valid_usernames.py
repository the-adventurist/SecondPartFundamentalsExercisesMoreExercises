def validation_and_printing(current_username):
    if not (3 <= len(current_username) <= 16):
        return
    wrong_user_name = False
    for current_symbol in current_username:
        if not(current_symbol.isalnum() or current_symbol == '_' or current_symbol == '-'):
            wrong_user_name = True
    if wrong_user_name:
        return
    print(current_username)


user_names = input().split(', ')
for current_username in user_names:
    validation_and_printing(current_username)
