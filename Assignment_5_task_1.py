#ASSINMENTS 5 Task 1: Create a Dictionary of Student Marks
# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

students = {
    "Aatif": 99,
    "Saif": 100,
    "Shuaib": 91,
    "Sahil":90
}

name = input("Enter the student's name : ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found in the dictionary.")