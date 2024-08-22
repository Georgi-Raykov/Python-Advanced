def gather_credits(credit, *args):
    current_credits = 0
    courses = []
    is_ready = False
    for items in args:

        course = items[0]
        credits = int(items[1])

        if course not in courses:
            courses.append(course)
            current_credits += int(credits)
        if current_credits >= credit:
            is_ready = True
            break
    result = ''
    if is_ready:
        result += f"Enrollment finished! Maximum credits: {current_credits}.\n" + ', '.join(sorted(courses))

    else:
        result += f"You need to enroll in more courses! You have to gather {credit - current_credits} credits more."
    return result


print(gather_credits(80, ('Basic', 27)))
print()
print(gather_credits(60, ('Basic', 27), ('Fundamentals', 27), ('Advanced', 30), ('Web', 30)))