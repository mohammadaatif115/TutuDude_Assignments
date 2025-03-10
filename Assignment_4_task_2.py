#ASSIGNMENT 4 Task 2: Write and Append Data to a File
 # Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.


file_name = "output.txt"

text = input("Enter text to write to the file: ")
with open(file_name, "w") as file:
    file.write(text + "\n")
print("Data successfully written to", file_name)

append_text = input("Enter additional text to append: ")
with open(file_name, "a") as file:
    file.write(append_text + "\n")
print("Data successfully appended.")

print("Final content of", file_name, ":")
with open(file_name, "r") as file:
    print(file.read())
