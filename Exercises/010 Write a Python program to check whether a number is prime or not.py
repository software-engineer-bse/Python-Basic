"""
Write a Python program to check whether a number is prime or not
"""
number = int(input("Enter number: "))
prime = True

for i in range(2,number):
    for j in range(2, number):
        if(i*j>number):
            break
        elif(i*j==number):
            prime = False
            
if(prime):
    print("The number is prime.")
else:
    print("The number is not prime.")