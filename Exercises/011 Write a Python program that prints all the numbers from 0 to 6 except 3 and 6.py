"""
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
"""
for i in range(7):
    if(i%3==0):
        continue
    print(i)