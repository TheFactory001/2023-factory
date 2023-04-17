# write a function to find the sum of a list of numbers
def sum_numbers(n1, n2):
    result = n1+n2
    print("The sum is", result)


number1 = 6
number2 = 8
sum_numbers(number1, number2)

# using return value


def sum_numbers(n1, n2):
    result = n1+n2
    return result


number1 = 6
number2 = 8
result = sum_numbers(number1, number2)
# print("The sum is", result)
