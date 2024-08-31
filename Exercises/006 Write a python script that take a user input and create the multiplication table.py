"""
Write a python script that take a user input and to create the multiplication table
(from 1 to 10) of that number.
"""

number = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{number} X {i} = {number*i}")