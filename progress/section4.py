
# # 2.write a function to determine the smallest value in a list
def calculate_smallest_value(any_list):
    any_list.sort()
    smallest_value = any_list[0]
    return smallest_value


my_list = [24, 22, 16, 50, 12, 34]
# print(calculate_smallest_value(my_list))

# # 2.write a function to determine the smallest value in a list
# # define my list
# my_list = (list)
# list = [24, 22, 16, 50, 12, 34,]
# # print(list)
# # sorting the list

# list = [24, 22, 16, 50, 12, 34,]
# list.sort()
# print(list)

# # smallest value could be determined by first element of sorted  list
# smallest_value = (list)
# list.sort()
# list = list[0]
# print(list)

# 3 write function to determin the mean of a list of numbers


def mean_of_list(list1):
    sum_list1 = sum(list1)
    count_list1 = len(list1)
    mean_of_list = sum_list1/count_list1
    return mean_of_list


# list1 = [24, 22, 16, 50, 12, 34]
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
print(calculate_median(users_list))
new_list = [40, 68, 20, 27, 30, 45, 32]
print(calculate_median(new_list))
# define my list
my_list = [24, 22, 16, 45, 10, 50, 12, 34]
# len of my list
num = len(my_list)
# print(num)
# sort my list
my_list.sort()
# print(my_list)
# if the sorted list have equal number on both sides, it could be the middle number

if num % 2 == 0:
    median1 = my_list[num//2]
    median2 = my_list[num//2-1]
    median = (median1+median2)/2
else:
    median = my_list[num//2]
# print(median)

# 5.write a unction to determine the largest value of a list


def calculate_largest_value(list1):
    list1.sort()
    largest_value = list1[-1]
    return largest_value


# my_list = [20, 45, 39, 50, 86, 23]
# # print(calculate_largest_value(my_list))

# #OR
# def max_number(list1):
#     if max_number(0):
#         result=1
#     else:


# 6. write a function to calculate the factorial of a number
def calculate_factorial(user_number):
    factorial = 1
    for each in range(1, user_number+1):
        factorial = factorial*each
        return factorial


num = 5
print(calculate_factorial)


# # # input a number
# (input("The number is:"))
# # get the range of the number
# for i in range(num):
print
# # factorial of a number could be the number multiply by all the integer between 1 and the number

# write a function that returns list of even numbers between 5 to 40
# Define num
num1, num2 = 5, 40
# iterate each number in list
# for num in range(num1, num2+1):
# print(num[num])
# to check the even numbers
# if num % 2 == 0:
# list(num)

# write a function that takes two arguments and return them in a string inside the function
# define the arguments
args = ("x", "y")
x = "python"
y = "programming language"
result = (x + y)
print(result)
# 1. write a function to get the count of a specific letter in a string
# define the string
str = "python is a programming language"
# the count of "a" in str
count = str.count

print(count("a"))
