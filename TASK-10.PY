#10 Write a Python program to calculate the percentage of marks obtained in an examination.

obtained_marks = float(input("Enter total marks obtained:"))
total_max_marks = 500
percentage = (obtained_marks / total_max_marks) * 100
print("Percentage:", percentage, "%")
