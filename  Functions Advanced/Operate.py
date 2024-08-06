def operate(operator, *args):
    def add():

        return sum(args)

    def subtract():
        if not args:
            return 0
        result = args[0]
        for arg in args[1:]:
            result -= arg
        return result

    def multiply():

        result = 1
        for arg in args:
            result *= arg
        return result

    def divide():

        result = args[0]

        for arg in args[1:]:
            result /= arg
        return result

    if operator == '-':
        return subtract()
    elif operator == '+':

        return add()
    elif operator == '*':
        return multiply()
    elif operator == '/':

        return divide()


print(operate("+", 1, 2, 3))
print(operate("-", 10, 4))
