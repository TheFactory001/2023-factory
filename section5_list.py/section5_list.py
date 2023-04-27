# # list
numbers = []
result = list(range(30+1))

print(result)

# # list of same number in multiple times
number = [2]
multiple_times = number*100
print(multiple_times)

# # combine list of strings and numbers
strings1 = ["a", "b", "c"]
numbers = [2]*5
combined = numbers+strings1
print(combined)

# print each character of a string in list
character = list("concatenate")
print(character)
print(len(character))

# function to check the range of a number


def check_range_of_list_of_number(result):
    result = list(range(number+1))
    return result


number = 30
# print(check_range_of_list_of_number(number))

# function of list of same number in multiple times


def same_number_in_multiple_time(multiple_time):
    multiple_time = number*30
    return multiple_time


number = [2]
print(same_number_in_multiple_time(number))
