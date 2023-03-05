tickets = [x.strip() for x in input().split(', ')]
winning_signs = ['@', '#', '$', '^']

for current_ticket in tickets:
    if len(current_ticket) != 20:
        print('invalid ticket')
        continue
    left_half = current_ticket[:len(current_ticket) // 2]
    right_half = current_ticket[len(current_ticket) // 2:]
    sequential_equal_signs_left_side = []
    sequential_equal_signs_right_side = []
    for current_sign in range(len(winning_signs)):
        for ticket_sign in range(len(left_half)):
            if winning_signs[current_sign] == left_half[ticket_sign] and not sequential_equal_signs_left_side:
                sequential_equal_signs_left_side.append(winning_signs[current_sign])
                continue
            if winning_signs[current_sign] == left_half[ticket_sign] \
                    and left_half[ticket_sign] == left_half[ticket_sign - 1]:
                sequential_equal_signs_left_side.append(winning_signs[current_sign])
                continue
            elif winning_signs[current_sign] == left_half[ticket_sign] \
                    and not (left_half[ticket_sign] == left_half[ticket_sign - 1]):
                sequential_equal_signs_left_side.clear()
                break
        for second_ticket_sign in range(len(right_half)):
            if winning_signs[current_sign] == right_half[second_ticket_sign] and not sequential_equal_signs_right_side:
                sequential_equal_signs_right_side.append(winning_signs[current_sign])
                continue
            if winning_signs[current_sign] == right_half[second_ticket_sign] \
                    and right_half[second_ticket_sign] == right_half[second_ticket_sign - 1]:
                sequential_equal_signs_right_side.append(winning_signs[current_sign])
                continue
            elif winning_signs[current_sign] == right_half[second_ticket_sign] \
                    and not (right_half[second_ticket_sign] == right_half[second_ticket_sign -1]):
                sequential_equal_signs_right_side.clear()
                break
    if 6 <= len(sequential_equal_signs_left_side) <= 9 and 6 <= len(sequential_equal_signs_right_side) <= 9\
            and sequential_equal_signs_left_side[0] == sequential_equal_signs_right_side[0]:
        if len(sequential_equal_signs_right_side) < len(sequential_equal_signs_left_side):
            print(f"ticket \"{current_ticket}\" - {len(sequential_equal_signs_right_side)}"
                  f"{sequential_equal_signs_left_side[0]}")
        else:
            print(f"ticket \"{current_ticket}\" - {len(sequential_equal_signs_left_side)}"
                  f"{sequential_equal_signs_left_side[0]}")

    elif len(sequential_equal_signs_left_side) == len(sequential_equal_signs_right_side) >= 10\
            and sequential_equal_signs_left_side[0] == sequential_equal_signs_right_side[0]:
        print(f"ticket \"{current_ticket}\" - {len(sequential_equal_signs_right_side)}"
              f"{sequential_equal_signs_right_side[0]} Jackpot!")
    else:
        print(f"ticket \"{current_ticket}\" - no match")
