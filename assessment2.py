# Write a program to display “Hello” if number entered is a multiple of five otherwise
#print “Bye.”

number = 1
if number % 5 == 0:
    print("Hello")
else:
    print("Bye")    


#Write a function with two arguments that adds 5 to the two argument and returns the
#total sum

def total_sum(x, y):
    x +=5
    y +=5
    result = x + y
    return result

print(total_sum(8,3))    



# Write a code that loops through a list of numbers to determine the greatest.

numbers = [12,34,76,45,3]
largest_so_far = numbers[0]
for value in numbers:
   
   if value > largest_so_far:
        largest_so_far = value
print(largest_so_far)



# Write a program that iterates through “Concatenation” and returns number of letters in
#the string

count = 0
string = "Concatenation"
for letters in string:
    count += 1
print(count)    




# Calculate the sum of all the odd numbers within the range of 10.
sum = 0
for value in range(10):
    if value%2 == 1:
        sum += value
print(sum)    


# Write a function checks the grades of students to return (“A” or “B” or “C”)

def grade(x):
    best_grade = 80
    good_grade = 60
    
    if x >= best_grade:
        print("A")
    elif best_grade > x >= good_grade:
        print("B")   
    else:
        print("C") 

grade(75)


# Write a program to print first 10 integers and their square using the while loop.

start = 0
end = 10

while start < end:
    square = start * start
    print(start, square) 
    start += 1  


#Write a program to print the sum of first 10 numbers.
sum = 0
start = 0
end = 10

while start <= end:
    sum += start
    start += 1
print(sum)





