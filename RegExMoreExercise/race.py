import re

participants = input().split(', ')
participants_results = dict.fromkeys(participants, 0)
pattern = r'[^\W]'
race_info = input()
while race_info != 'end of race':
    matches = re.findall(pattern, race_info)
    name = ''
    distance = 0
    for match in matches:
        if match.isdigit():
            distance += int(match)
        else:
            name += match
    distance = int(distance)
    if name in participants_results:
        participants_results[name] += distance
    race_info = input()
sorted_participants_results = sorted(participants_results.items(), key=lambda x: -x[1])
print(f"1st place: {sorted_participants_results[0][0]}")
print(f"2nd place: {sorted_participants_results[1][0]}")
print(f"3rd place: {sorted_participants_results[2][0]}")
