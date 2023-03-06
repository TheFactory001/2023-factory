# sum of all odd numbers within the range of 10
num = 10
oddsum = 0
for int in range(1, num+1):
    if int % 2 != 0:
        oddsum += int
print(oddsum)
