def softuni_students(*args, **kwargs):
    valid_id = {}
    invalid_id = []

    for item in args:
        id = item[0]
        student_name = item[1]
        if id in kwargs:
            valid_id[student_name] = kwargs[id]
        else:
            invalid_id.append(student_name)
    result = ''
    sorted_students = sorted(valid_id.items(), key=lambda x: x[0])
    for student, program in sorted_students:
        result += f"*** A student with the username {student} has successfully finished the the course {program}!\n"
    if invalid_id:
        result += f"!!! Invalid course students: {', '.join(invalid_id)}"
    return result


print(softuni_students(('id_7', 'Silvester1'), ('id_32', 'Katq21'), ('id_7', 'The programer'),
      id_76='Spring Fundamentals', id_7='Spring Advanced'))
print()
print(softuni_students(('id_1', 'Kaloyan9905'), id_1='Python Web Framework'))