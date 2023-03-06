# write a function to check the grades of students to return ("A" or "B" or "C")
gradeA = 80
gradeB = 65
gradeC = 55
student_grades = int(input())
if student_grades >= 80:
    print("A")
elif student_grades >= 65 and student_grades < 80:
    print("B")
elif student_grades >= 55 and student_grades < 65:
    print("C")
else:
    print("D")
