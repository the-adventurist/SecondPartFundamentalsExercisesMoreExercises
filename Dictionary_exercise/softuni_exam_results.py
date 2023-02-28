users_max_points = {}
language_submission_count = {}

data = input()
while data != 'exam finished':
    data_args = data.split('-')
    if len(data_args) == 3:
        username, language, points = data_args
        points = int(points)
        if username not in users_max_points:
            users_max_points[username] = 0
        if points > users_max_points[username]:
            users_max_points[username] = points
        language_submission_count[language] = language_submission_count.get(language, 0) + 1
    else:
        username = data_args[0]
        if username in users_max_points:
            del users_max_points[username]
    data = input()

print('Results:')
for username, points in users_max_points.items():
    print(f'{username} | {points}')

print('Submissions:')
for language, count_submission in language_submission_count.items():
    print(f'{language} - {count_submission}')
