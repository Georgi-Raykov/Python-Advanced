def rectangle(length, width):
    def perimeter():
        perimeter = f"Rectangle perimeter: {length * 2 + width * 2}"
        return perimeter

    def area():
        area = f"Rectangle area: {length * width}"
        return area

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    return area() + '\n' + perimeter()


print(rectangle(2, 10))
