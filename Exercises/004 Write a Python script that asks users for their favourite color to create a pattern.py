"""
Write a Python script that asks users for their favourite color to create a pattern. Create the following
output (assuming blue is the chosen color)
                            blueblueblueblueblueblueblueblueblueblue
                            blue                                blue
                            Blueblueblueblueblueblueblueblueblueblue
"""
color = input("Enter color: ")
for i in range(3):
    if(i%2==1):
        print(color,end="")
        print(len(color)*" "*8,end="")
        print(color)
    else:
        print(color*10)