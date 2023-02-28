def contest_and_password_validation(curr_contest,password_ , receiving_contests):
    if curr_contest in receiving_contests:
        if receiving_contests[curr_contest] == password_:
            return True


contest_passwords = {}
results = {}
taken_part = {}

data = input()
while data != 'end of contests':
    contest, password = data.split(':')
    contest_passwords[contest] = password
    data = input()

data = input()
while data != 'end of submissions':
    contest, password, username, points = data.split('=>')
    points = int(points)
    valid = contest_and_password_validation(contest, password, contest_passwords)
    if valid:
        if username not in results:
            results[username] = {}
        if contest not in results[username]:
            results[username][contest] = 0
        if results[username][contest] < points:
            results[username][contest] = points

    data = input()

best_total_points = 0
the_best_participant = None

for username, information in results.items():
    sum_total_points = sum(information.values())
    if best_total_points < sum_total_points:
        the_best_participant = username
        best_total_points = sum_total_points

print(f"Best candidate is {the_best_participant} with total {best_total_points} points.")
sorted_results = sorted(results.items(), key=lambda x: x)

print('Ranking:')
for username, information in sorted_results:
    print(username)
    sorted_information = sorted(information.items(), key=lambda x: -x[1])
    for contest, points in sorted_information:
        print(f'#  {contest} -> {points}')
