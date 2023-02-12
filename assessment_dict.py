#  Convert two lists into a dictionary
#   The update() method assign values from an iterable of key/value pairs. 
# def conversion():

#     keys = ['Ten','Twenty', 'Thirty', 'Forty','Fifty']
#     values = [10, 20, 30, 40, 50 ,60 ]

# derived_dict = {}
# if len(keys) == len(values):
#     print(f"values useable")
#     for i in range(len(keys)):
#         derived_dict.update({keys[i] : values[i]})
#     print(derived_dict)
# else:
#     print("Reassign the variables")    





#  Check for key in a dictionary
def check(letter):
    sample_dict = {'d': 4, 'f' : 5 ,'g': 20, 'l': 30}

    for data in sample_dict.keys():
        if letter in data:
            print(letter)

            
#print(check('d'))  
          



# The enumerate() function adds the key of the enumerate object.
# Geometric Progression
# Formular : U = a*r^n-1
def geometric_progression(a,r,n):
# a = first value , r = common ratio , n = variable
    geometric_1 = []
    values = {}  
    
    for data in range(n+1):
        value = a * pow(data,n-1)
        geometric_1.append(value)
    values = dict(enumerate(geometric_1, 1)  )  
    return values 

#print(geometric_progression (5,2,5))      



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

    for i in modal_numbers.values():
        if i >= modal_count:
            modal_count = i

    key = [k for k, v in modal_numbers.items() if v == modal_count ]        
    modal_text= " The mode is" ,key, "is  with" ,modal_count," variables"
    return modal_numbers , modal_text

  

x,y = mode([2,7,4,5,7,6,7,5,8,9,2,4,5,6,67,89,7])
print(x)
print(y)

# Sum OF VALUES IN DICTIONARY

dict_s = {'a': 4 , 'b': 8, 'c': 9, 'd': 7}
sum = 0

for num in dict_s.values():
    sum += num
    
#print(sum)    








