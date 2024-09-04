"""
Write a function called absolute_num that accepts one parameter num, the function should return only positive value.
"""
def absolute_num(num):
    if(num<0):
        num = num*-1
        return num
    else:
        return num
    
print(absolute_num(-1))
print(absolute_num(0))
print(absolute_num(1))