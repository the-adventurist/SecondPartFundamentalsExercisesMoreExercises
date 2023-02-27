teachers_dictionary = {}
pupils = int(input())

for _ in range(pupils):
    pupil = input()
    grade = float(input())
    teachers_dictionary[pupil] = teachers_dictionary.get(pupil, [])
    teachers_dictionary[pupil].append(grade)

teachers_dictionary = {name: sum(grade) / len(grade) for (name, grade) in teachers_dictionary.items()
                       if sum(grade) / len(grade) >= 4.5}
for name, grade in teachers_dictionary.items():
    print(f'{name} -> {grade:.2f}')
