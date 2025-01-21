# Call by value
x1 = 2
y1 = x1
y1 = y1+2
print(x1)
print(y1)

# Call by reference
x2 = [2,1]
y2 = x2
y2[0] = 4
print(x2)
print(y2)