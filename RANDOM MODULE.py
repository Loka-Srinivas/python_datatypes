import random
print(random.random())


import random
print(random.randint(1,100))


import random
list1=['apple','banana','mango','orange']
print(random.choice(list1))



a=[1,2,3]
sum=0
for i in a:
    sum=sum*10+i
    sum+=0
print(sum)
print(list(str(sum)))    