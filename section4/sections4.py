# 1. write a function to get the count of a specific letter in a string
def get_count_of_letter(check_letter):
    count_of_my_letter = ""
    for each_character in check_letter:
        if each_character == "g":
            count_of_my_letter += each_character
    return count_of_my_letter


# print(len(get_count_of_letter("programming languageS")))


# 2.write a function to determine the smallest value in a list
def calculate_smallest_value(any_list):
    any_list.sort()
    smallest_value = any_list[0]
    return smallest_value


my_list = [24, 22, 16, 50, 12, 34]
# print(calculate_smallest_value(my_list))
user_list = [9, 6, 7, 4, 8, 3, 1, 2]
# print(calculate_smallest_value(user_list))


# 3 write function to determin the mean of a list of numbers


def mean_of_list(list1):
    sum_list1 = sum(list1)
    count_list1 = len(list1)
    mean_of_list = sum_list1/count_list1
    return mean_of_list


list1 = [24, 22, 16, 50, 12, 34]
# print(mean_of_list(list1))


# 4. write a function to determine the median of a list of numbers
def calculate_median(user_list):
    num = len(user_list)
    user_list.sort()
    if num % 2 == 0:
        median1 = user_list[num//2]
        median2 = user_list[num//2-1]
        median = (median1+median2)/2
    else:
        median = user_list[num//2]
    return median


users_list = [27, 16, 45, 46, 10, 50, 12, 34]
# print(calculate_median(users_list))
new_list = [40, 68, 20, 27, 30, 45, 32]
# print(calculate_median(new_list))

# 5.write a unction to determine the largest value of a list


def calculate_largest_value(list1):
    list1.sort()
    largest_value = list1[-1]
    return largest_value


my_list = [20, 45, 39, 50, 86, 23]
# print(calculate_largest_value(my_list))


# 6. write a function to calculate the factorial of a number


def calculate_factorial(num):
    factorial = 1
    for each in range(1, num+1):
        factorial = factorial*each
    return factorial


number = 5
# print(calculate_factorial(number))

# 7.  write a function that returns list of even numbers between 5 to 40


def get_list_of_even_numbers(min_even_number, max_even_number):
    list_of_even_numbers = []
    for each_number in range(min_even_number, max_even_number+1):
        if each_number % 2 == 0:
            list_of_even_numbers.append(each_number)
    return list_of_even_numbers


min_even_number = 5
max_even_number = 40
print(get_list_of_even_numbers(min_even_number, max_even_number))

# 8. write a function that takes two arguments and return them in a string inside the function


def combine_two_strings(first_string, second_string):
    result = first_string + " " + second_string
    return result


my_first_string = "Esther"
my_second_string = "John"
# print(combine_two_strings(my_first_string, my_second_string))
