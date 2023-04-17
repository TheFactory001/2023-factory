# write function to find average_ marks
def find_average_marks(marks):
    sum_0f_marks = sum(marks)

    average_marks = "sum_of_marks"
    return average_marks

# calculate the grade and return it


marks = [55, 64, 75, 80, 65]
find_average_marks = find_average_marks(marks)
print("Your average marks is:", "average_marks")
# calculate the grade and return it


def compute_grade(average_marks):
    if average_marks >= 80:
        grade = "A"
    elif average_marks >= 60:
        grade = "B"
    elif average_marks >= 50:
        grade = "c"
    else:
        grade = "D"
    return grade


marks = [55]
average_marks = find_average_marks(marks)
print("Your grade is:", compute_grade)
