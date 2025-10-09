# 31/07/2025
# NESTED IF-ELSE STATEMENTS PROBLEMS IN PYTHON

# PART-A:-


bottles = int(input("Enter bottles: "))
regular = input("Regular customer? (yes/no): ")

if bottles > 2:
    if regular == "yes":
        print("15% discount")
    else:
        print("5% discount")
else:
    print("No discount")


fuel = int(input("Fuel level (%): "))
vehicle = input("Enter vehicle (car/bike): ")

if fuel < 25:
    if vehicle == "car":
        print("Refuel soon at a petrol station.")
    elif vehicle == "bike":
        print("Refuel at nearest pump.")
    else:
        print("Check vehicle type.")


grade = int(input("Enter grade: "))
income = int(input("Enter income (in lakhs): "))

if grade > 85:
    if income < 3:
        print("Full Scholarship")
    elif income <= 6:
        print("Half Scholarship")
    else:
        print("No Scholarship")


cart = int(input("Enter cart value: "))
pay = input("Payment method (card/UPI): ")

if cart > 1000:
    if pay == "card":
        print("10% off")
    elif pay == "UPI":
        print("15% off")
    else:
        print("No discount")
else:
    print("No discount")


age = int(input("Enter age: "))
vaccine = input("Vaccinated? (yes/no): ")

if age >= 18:
    if vaccine == "yes":
        print("Allowed to dine in")
    else:
        print("Takeaway only")
else:
    print("You must be at least 18 to dine here.")


age = int(input("Enter age: "))
height = int(input("Enter height (cm): "))

if 14 <= age <= 18:
    if height > 160:
        print("Eligible")
    else:
        print("Not eligible (too short)")
else:
    print("Not eligible (age out of range)")


# PART-B:-

color = input("Enter light color: ")
print("Go" if color == "green" else "Stop")


age = int(input("Enter age: "))
print("Adult Ticket" if age >= 18 else "Child Ticket")


amount = int(input("Enter amount: "))
print("You get a free gift!" if amount >= 500 else "No gift")


loc = input("Enter location: ")
print("Delivery Fee: Rs20" if loc == "local" else "Delivery Fee: Rs50")


temp = float(input("Enter temperature: "))
print("High Fever" if temp >= 100 else "Normal")


hour = int(input("Enter hour (0-23): "))
print("Good Morning" if hour < 12 else "Good Afternoon" if hour < 17 else "Good Evening")


# Bonus Challenge: Electricity Bill Calculator


units = int(input("Enter units: "))
usage = input("Usage type (residential/commercial): ")

if units < 100:
    print("Bill = Free")
elif units <= 300:
    if usage == "residential":
        print("Bill =", units * 5)
    else:
        print("Bill =", units * 8)
else:
    print("Bill =", units * 10)
