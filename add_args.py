#2. Write a function with the two arguments that adds 5 to the two arguments and return the total sum

def calculate_total_sum(value, arg):
    total_sum = 0
    for number in (value, arg):
        total_sum += number + 5
    print(total_sum)

#calculate_total_sum(5, 4)


#Write a code that loops through a list of numbers to determine the greatest
def max_value(*int):
    value = 0
    for i in range(len(int)):
       print(list(i))

#max_value(2, 3, 4, 5, 5)

numbers = [2, 3, 7, 9, 4]
def get_maximum_value(my_list):
    largest_so_far = my_list[0]
    for number in my_list:
        if number > largest_so_far:
            largest_so_far = number
    return largest_so_far

result = get_maximum_value(numbers) 
#print(result)  

#Calculate the sum of all the odd numbers within the range of 10.
n = 10
sum = 0
for i in range(n):
    if i%2 == 1:
        sum += i
print(sum)

#1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#1, 3, 5, 7, 9
#25