# function with two arguments that adds 5 to the two argument and returns the total sum
def calculate_total_sum(numbers):
    total_sum = sum(numbers)+5
    for number in numbers:
        return total_sum


numbers = [3, 6]
print(calculate_total_sum(numbers))

# without using loop


def calculate_total_sum(numbers):
    total_sum = sum(numbers)+5
    return total_sum


numbers = [3, 6]
# print(calculate_total_sum(numbers))
