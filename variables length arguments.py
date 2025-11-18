

# Varible length arguments: It is used to pass multiple values to a single parameters in a function


 
def number(*nums):
    Add=0
    for i in nums:      
        Add+=i
    return Add 

print(number(1,2,3,4,5,6,7,8,9,10))  
        

def number(*nums):
    mul=1
    for i in nums:
        mul*=i
    return mul  

print(number(1,2,3,4,5,6,7,8,9,10))    




# Varible Length Keyword Arguments:
    
   
def details(**urdetails):
    for i,j in urdetails.item():
        print(f'{i}:{j}')
details            