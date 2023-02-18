#1. Write a program to display "Hello" if the number entered is a multiple of five, otherwise print "Bye"

value = int(7865745)
if value%5 == 0:
    print("Hello")
else:
    print("Bye") 


#2. Write a function with the two arguments that adds 5 to the two arguments and return the total sum
'''
def calculate_total_sum(value, arg):
    total_sum = 0
    for number in (value, arg):
        total_sum += number + 5
    print(total_sum)

calculate_total_sum(5, 4)
'''

'''
#Write a code that loops through a list of numbers to determine the greatest
def max_value(*int):
    value = 0
    for i in range(len(int)):
        print(list(i))

max_value(2, 3, 4, 5, 5)
'''

#Calculate the sum of all the odd numbers within the range of 10.
'''					
n = int(input(10))
sum = 0
for i in range(1, n+1, 2):
    sum += i
print(sum)
'''
