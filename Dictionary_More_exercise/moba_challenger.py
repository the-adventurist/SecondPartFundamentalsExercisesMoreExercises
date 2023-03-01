players_positions_skills = {}
players_total_skills = {}

data = input()
while data != 'Season end':
    data_args = data.split(' -> ')
    if len(data_args) > 1:
        player, position, skill = data_args
        skill = int(skill)
        if player not in players_positions_skills:
            players_positions_skills[player] = {}
        if position not in players_positions_skills[player]:
            players_positions_skills[player][position] = 0
        if players_positions_skills[player][position] < skill:
            difference = skill - players_positions_skills[player][position]
            players_positions_skills[player][position] = skill
            players_total_skills[player] = players_total_skills.get(player, 0) + difference
    else:
        first_player, second_player = data.split(' vs ')
        killed_player = False
        for current_player, current_position in players_positions_skills.items():
            for this_position, this_skill in current_position.items():
                for second_current_player, second_current_position in players_positions_skills.items():
                    for second_this_position, second_this_skill in second_current_position.items():
                        if current_player == first_player and second_current_player == second_player \
                                and this_position == second_this_position \
                                and this_skill != second_this_skill:
                            if players_total_skills[first_player] > players_total_skills[second_player]:
                                killed_player = True
                                del players_positions_skills[second_player]
                                del players_total_skills[second_player]
                            else:
                                killed_player = True
                                del players_positions_skills[first_player]
                                del players_total_skills[first_player]
                        if killed_player:
                            break
                    if killed_player:
                        break
                if killed_player:
                    break
            if killed_player:
                break
    data = input()

sorted_players_total_skills = sorted(players_total_skills.items(), key=lambda x: (-x[1], x[0]))

for player, total_skill in sorted_players_total_skills:
    print(f'{player}: {total_skill} skill')
    for this_player, data in players_positions_skills.items():
        sorted_data = sorted(data.items(), key=lambda x: (-x[1], x[0]))
        if player == this_player:
            for position, skill in sorted_data:
                print(f'- {position} <::> {skill}')
