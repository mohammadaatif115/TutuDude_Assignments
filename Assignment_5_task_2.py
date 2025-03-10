# # ASSIGNMENTS 5 Task 2: Demonstrate List Slicing 
# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

l = list(range(1,11))
print('Original list: ',l)
m = l[:5]
print('Extracts first five elements: ',m)
print('Reverse extracted elements: ',m[::-1])