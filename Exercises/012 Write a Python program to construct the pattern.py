"""
Write a Python program to construct the pattern.
1
22
333
4444
55555
"""
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()