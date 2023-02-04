# Write a Python function to gets sequence of numbers (arithmetic progresssion)
# Using formular U = a + (n+1)d

def arith_progression(n,s,d):
    # s = start number, n = required variable, d = common difference  
    numbers = []
    value_n = s + (n+1)*d
    
    for data in range(n+1):
        value = s + (data+1)*d
        numbers.append(value)
    print(f"The {n}th value in the progression is {value_n} ")      
    return(numbers)  
   
        

#print(arith_progression(5,4,45))



def mode(numbers):
    values = numbers
    values.sort()
    modal_numbers = {}
    modal_count = 0
    
    for number in values:
        if number in modal_numbers:
            modal_numbers[number] += 1
        else:
            modal_numbers[number] = 1

    for i in modal_numbers[1]:
        if i >= modal_count:
            modal_count = i
    return modal_count         

  

print(mode([2,7,4,5,2,6,7,5,8,9,7,4,5,6,67,89,7]))   



# FINGING MODE IN LIST OF VALUES
# The parameter is the value I am trying to find
def Mode(value):
    values = [45,45,3,5,7,45,0,5,3,9,0,1,3,45]
    count = 0

    for data in values:
        if data == value:
            count += 1

    return(f"The mode of {value} is {count}")  

#print(Mode(0))   

                 



    
# Write a Python function to find the Max of numbers

def max(*numbers):
    values = list(numbers)
    max_value = 0

    for value in values:
        if value >= max_value:
            max_value = value
    return (f"The maximum value is {max_value}")     

#print(max(-1,23,6,7,8))       






















