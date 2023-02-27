companies = {}

info = input()
while info != 'End':
    company, employees_id = info.split(' -> ')
    if company not in companies:
        companies[company] = []
    if employees_id not in companies[company]:
        companies[company].append(employees_id)
    info = input()

for company, employees_id in companies.items():
    print(company)
    for current_id_employee in employees_id:
        print(f'-- {current_id_employee}')

