def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}
dictionary1 = {}
print(kwargs_length(**dictionary))
print(kwargs_length(**dictionary1))
