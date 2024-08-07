def age_assignment(*args, **kwargs):
    new_assignment = {}
    for name in args:
        first_letter = name[0]
        if first_letter in kwargs:
            new_assignment[name] = kwargs[first_letter]
    sorted_names = sorted(new_assignment.items(), key=lambda x: x[0])
    result = []
    for key, value in sorted_names:
        result.append(f"{key} is {value} years old.")
    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))