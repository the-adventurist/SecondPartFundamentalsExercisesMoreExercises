contests = {}
individual_statistics = {}

data = input()
while data != 'no more time':
    username, contest, points = data.split(' -> ')
    points = int(points)
    if contest not in contests:
        contests[contest] = {}
    if username not in contests[contest]:
        contests[contest][username] = 0
    if contests[contest][username] < points:
        contests[contest][username] = points
    individual_statistics[username] = individual_statistics.get(username, 0) + points
    data = input()

sorted_ind_statistic = sorted(individual_statistics.items(), key=lambda x: -x[1])

for contest, user_data in contests.items():
    print(f'{contest}: {len(user_data)} participants')
    sorted_user_data = sorted(user_data.items(), key=lambda kvpt:(-kvpt[1], kvpt[0]))
    counter = 0
    for name, points in sorted_user_data:
        counter += 1
        print(f'{counter}. {name} <::> {points}')

print('Individual standings:')
counter = 0
for username, total_points in sorted_ind_statistic:
    counter += 1
    print(f'{counter}. {username} -> {total_points}')
