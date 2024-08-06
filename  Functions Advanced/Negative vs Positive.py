def find_negative_positive(*args):
    positive = 0
    negative = 0
    for num in args:
        if num > 0:
            positive += num
        else:
            negative += num
    return negative, positive


nums = [int(x) for x in input().split()]

negative_sum, positive_sum = find_negative_positive(*nums)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
