class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def car_info(self):
        print(f"Car Brand:{self.brand},Model:{self.model}")

car1=Car("Toyota","Innova")
car2=Car("Hyundai","Creta")
car3=Car("Tata","Harrier")

car1.car_info()
car2.car_info()
car3.car_info()



class BankAccount:
    def __init__(self):
        self.__balance=0  
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited:{amount}")
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdraw:{amount}")
        else:
            print("")
    def get_balance(self):
        return self.__balance


account=BankAccount()
account.deposit(5000)
account.withdraw(2000)
print("Current Balance:", account.get_balance())



class Student:
    def __init__(self):
        self.__marks=0
    def marks(self):
        return self.__marks
    def marks(self, value):
        if 0<=value<=100:
            self.__marks=value
        else:
            print("")


s=Student()
s.marks=85
print("Marks:", s.marks)
s.marks=120  

