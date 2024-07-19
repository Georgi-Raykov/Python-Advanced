numbers = tuple(map(float, input().split()))

end_result = {}

for number in numbers:

    if number not in end_result:

        end_result[number] = numbers.count(number)


for key, value in end_result.items():

    print(f"{key} - {value} times")
