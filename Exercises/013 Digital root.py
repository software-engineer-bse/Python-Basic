"Digital root"
def digital_root(number):
    total_sum = 0
    for i in range(len(number)):
        num_1 = int(number[i])
        total_sum = total_sum + num_1
        
    if(len(str(total_sum))==1):
        return total_sum
    else:
        return digital_root(str(total_sum))
    
var = digital_root("1234")
print(var)