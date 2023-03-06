tickets = [x.strip() for x in input().split(', ')]
winning_signs = ['@', '#', '$', '^']

for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue
    has_no_winning_ticket = True
    left_side = ticket[:len(ticket)//2]
    right_side = ticket[len(ticket)//2:]
    for winning_sign in winning_signs:
        sequential_l_signs = []
        sequential_r_signs = []
        for sign in range(len(left_side)):
            if winning_sign == left_side[sign] and not sequential_l_signs:
                sequential_l_signs.append(left_side[sign])
            elif winning_sign == left_side[sign] and left_side[sign - 1] == left_side[sign]:
                sequential_l_signs.append(left_side[sign])
        for sign in range(len(right_side)):
            if winning_sign == right_side[sign] and not sequential_r_signs:
                sequential_r_signs.append(right_side[sign])
            elif winning_sign == right_side[sign] and right_side[sign - 1] == right_side[sign]:
                sequential_r_signs.append(right_side[sign])
        if len(sequential_l_signs) == len(sequential_r_signs) == 10:
            print(f"ticket \"{ticket}\" - {len(sequential_l_signs)}{winning_sign} Jackpot!")
            has_no_winning_ticket = False
        elif 6 <= len(sequential_l_signs) <= 10 and 6 <= len(sequential_r_signs) <= 10:
            if len(sequential_r_signs) <= len(sequential_l_signs):
                print(f"ticket \"{ticket}\" - {len(sequential_r_signs)}{winning_sign}")
                has_no_winning_ticket = False
            elif len(sequential_l_signs) <= len(sequential_r_signs):
                print(f"ticket \"{ticket}\" - {len(sequential_l_signs)}{winning_sign}")
                has_no_winning_ticket = False
    if has_no_winning_ticket:
        print(f"ticket \"{ticket}\" - no match")
