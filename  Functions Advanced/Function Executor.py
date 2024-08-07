def func_executor(*args):
    result = []

    for func, func_parameter in args:
        func_result = func(*func_parameter)
        result.append(f"{func.__name__} - {func_result}")
    return '\n'.join(str(x) for x in result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)

    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)

    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))

                    ))
print(func_executor((make_upper, ("Python", "softUni")), (make_lower, ("PyThOn",)),

                    ))
