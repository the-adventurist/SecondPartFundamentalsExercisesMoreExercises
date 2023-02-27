courses = {}
info = input()

while info != 'end':
    course_name, student_name = info.split(' : ')
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    info = input()

for course, students in courses.items():
    print(f'{course}: {len(courses[course])}')
    for name in students:
        print(f"-- {name}")
