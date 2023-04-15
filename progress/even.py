

# 1. write a function to get the count of a specific letter in a string

# A carton contains balls with different colours
carton = "programming"
# define the ball to count
ball_to_count = "i"
# put a particular coloured ball in an new_carton
count_of_coloured_ball = 0
# To get the number of the balls in carton
for each_ball in carton:
    print(each_ball)
# each ball may be counted to get the count of the coloured ball
    if each_ball == ball_to_count:
        # to get the count of the coloured ball could be count of coloured ball + 1
        count_of_coloured_ball = count_of_coloured_ball + 1
print(count_of_coloured_ball)


# write a function that takes two arguments and return them in a string inside the function

# define the two fruits to make fruit salad
first_plate_of_fruit = "Apple"
second_plate_of_fruit = "Water_melon"
# add the two  plates of fruits together to get a single plate of fruit salad
plate_of_fruit_salad = first_plate_of_fruit + " "+"&"+" " + second_plate_of_fruit
print(plate_of_fruit_salad)


# writing a function that checks through(loop) iterables for a paritcular condition (logic), it then returns all valid item in another variable\
# using a function that returns as many 'e' as found in a given string: it returns the e_S in a string
def find_e_s(my_string_aka_my_iterable):
    # 1st step: know ur main iterable, such as : a list, a string, a dictionary, tuple, range;
    # in this function, my main iterable is my_string_aka_my_iterable:  its strings, collection of characters

    # step 2: you create/define an empty container or carton where you will store all the items that meet your condition
    container_for_my_e_s = ""
    # step 3: write the loop that checks through my main iterable
    for each_item in my_string_aka_my_iterable:  # this means for each item that can be seen in my iterable
        # step 4, write the logic or the condition, so for each item in the loop, it checks if it meets the condition, if true/yes, it executes whatever is in the logic
        if each_item == "e":
            # this might be confusing, but its common in programming to write a = a +b as a+=b, its just shorter and cleaner.
            container_for_my_e_s += each_item
    return container_for_my_e_s


print(find_e_s("hello to new ones"))


# writing a function that checks through(loop) iterables for a paritcular condition (logic), it then returns all valid item in another variable\
# using a function that returns as many 'e' as found in a given string: it returns the e_S in a string
def find_e_s(my_string_aka_my_iterable):
    # 1st step: know ur main iterable, such as : a list, a string, a dictionary, tuple, range;
    # in this function, my main iterable is my_string_aka_my_iterable:  its strings, collection of characters

    # step 2: you create/define an empty container or carton where you will store all the items that meet your condition
    container_for_my_e_s = ""
    # step 3: write the loop that checks through my main iterable
    for each_item in my_string_aka_my_iterable:  # this means for each item that can be seen in my iterable
        # step 4, write the logic or the condition, so for each item in the loop, it checks if it meets the condition, if true/yes, it executes whatever is in the logic
        if each_item == "t":
            # this might be confusing, but its common in programming to write a = a +b as a+=b, its just shorter and cleaner.
            container_for_my_e_s += each_item
    return container_for_my_e_s


print(len(find_e_s(("esther"))))
