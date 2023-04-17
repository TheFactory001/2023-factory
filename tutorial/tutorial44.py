# # write a code that loops through a list of numbers to determine the greatest
def max_number(number_list):
    for number in number_list:
        max_number = max(number_list)
    return max_number


my_list = [20, 45, 39, 50, 86, 23]
print(max_number(my_list))

#  define my_lists
# my_lists = [20, 45, 39, 50, 86, 23]
# # loop through my lists
# for number in my_lists:
#     # print(number)
#     # To determine the greatest could be max number equals to  max of number list
#     max_number = max(my_lists)
# print(max_number)
