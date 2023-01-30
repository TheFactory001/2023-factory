# Function gets the number of specific letter in a string
def greets(letter):
    greeting = "Hello boring Old World"
    get_greeting = list(greeting)
    # get values of "O"
    count = 0
    for alpha in get_greeting:
        if alpha.lower() == letter:
            count += 1
    print( f"The count of letter {letter} are {count}"  )   

#greets("l")


# Determine mean, median and mode of the 20 random number
def mean(*numbers):
    total = 0
    count = len(numbers)
    for value in numbers:
        total += value       
    print(f"Sum = {total}") 

    average = total/count 
    print(f"Mean value is {average}")

mean(4,5,6,7)



def median(*numbers):
   
    values = list(numbers)
    values.sort()
    # print(type(values))
    count = len(numbers) 
    
    if count%2 == 1:
        middle_odd = int(count/2 + 1/2)
        print(values[middle_odd])
    elif count%2 == 0:    
        mid_even = int(count/2)-1
        s_average = values[mid_even] + values[mid_even +1] 
        mid = s_average/2  
        print(mid)

    # for i in values:
    #     if count%2 == 1:
    #         print(values[middle_odd])


    #     else:
    #         s_average = values[mid_even] + values[mid_even +1] 
        #     mid = s_average/2  
        # print(mid)

# 2,3,4,7,9,12
median(2,3,7,12,4,9)


















