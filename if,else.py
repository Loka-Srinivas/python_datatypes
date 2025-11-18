job=True
money=True
skills=True

if(job==True and money==True and skills==True):
    print("Do you whatever you not marriage")

elif job==True:
    print("Go to job")
    
elif money==True:
    print("Go to a Business")

elif skills==True:
    print("Go to freelance")

else:
    print('Join Coaching Centre')


money=int(input("enter your money:"))

if money>1000:
    print("order a cofffe")

elif money<500:
    print("order a tea")

else:
    print("order a water")        



age=int (input("enter your age:"))
if age>18:
    print("eligible for vote")
else:
    print("not eligible for vote")



#Ternary Operator Example
    print('eligible for vote' if age>=18 else 'not eligible for vote')

        

percentage = int(input("Enter your percentage:"))

if percentage >= 90:
    print("O grade is obtained")

elif percentage >= 80:
    print("A grade is obtained")

elif percentage >= 70:
    print("B grade is obtained") 

elif percentage >= 60:
    print("C grade is obtained")

elif percentage >= 50:
    print("D grade is obtained")

else:
    print("F grade is obtained")

