# Write a Python program that computes n+nn+nnn for a number n.

n = 3
result = n+n*n+n*n*n

#print(result)

#Store three integers in x, y and z. Print their product

x = 1
y = 5
z = 7

#print(x * y * z)


#Write a Python program to determine whether a given integer is even or odd

x = 5
if x//2 == 0:
    print("Value is even")
else:
    print("Value is odd")

#Check type of following: 15, "CodesDope", 16.2, 9.33333333333333
#print(type(15))
#print(type("CodesDope"))
#print(type(16.2))
#print(type(9.33333333333))

# Join two string using '+'. E.g.-"Codes"+"Dope"
#print("Code"+"Dope")

#Store two values in x and y, swap their values, and print the new values
x = 5
y = 10
z = x
x = y
y = z
#print("x:",x, " ""y:",y)

#Print the remainder of 101 divided by 25
#print(101 % 25)

# Print "welcome" from a String "You are welcome to TheFactory"
greeting ="You are welcome to TheFactory"
print(len(greeting))
print(greeting[8])
print(greeting[14])
print(greeting[8:15])
print(greeting[19:])

#Print type of following: False, [1,2,3], {"a": 1}
print(type(False))
print(type([1,2,3]))
print(type({"a":1}))
