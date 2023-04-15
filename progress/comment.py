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
