# determine the smallest value of a list
# define my list
# my_list = [34, 12, 40, 45, 63, 14]
# # sort my list
# my_list.sort()
# print(my_list)
# # to determine the smallest value could be the first element of my sorted list
# smallest_value = my_list[0]
# print(smallest_value)


def calculate_smallest_value(any_list):
    any_list.sort()
    smallest_value = any_list[0]
    return smallest_value


my_list = [34, 12, 40, 45, 63, 14]
print(calculate_smallest_value(my_list))
daniel_list = [6, 4, 26, 34]
print(calculate_smallest_value(daniel_list))
