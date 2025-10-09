# 01/08/2025
# LOOPSIN PYTHON


# SECTION:-1 Easy while Loop Tasks:-


i = 1
while i <= 5:
    print(i)
    i += 1


i = 2
while i <= 10:
    print(i)
    i += 2


i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum =", total)


n = input("Enter number: ")
i = 0
while i < len(n):
    print(n[i])
    i += 1


i = 10
while i >= 1:
    print(i)
    i -= 1


# SECTION:-2 Easy for Loop Tasks:-


for i in range(1, 11):
    print(i)


for ch in "banana":
    print(ch)


for i in range(1, 6):
    print(i * i)


nums = [2, 5, 8, 9, 10]
for n in nums:
    if n % 2 == 0:
        print(n)


for i in range(1, 21):
    if i % 3 == 0:
        print(i)


# SECTION:-3 Easy Nested Loop Tasks:-


for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()


for i in range(3):
    for j in range(1, 4):
        print(j, end=" ")
    print()


for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


for i in range(1, 11):
    print("2 x", i, "=", 2 * i)


words = ["hi", "ok"]
for w in words:
    for ch in w:
        print(ch)
        
        
# SECTION:-4 Loops with Conditions:-        


for i in range(1, 11):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")
        
        
for i in range(5):
    n = int(input("Enter number: "))
    if n % 2 == 0:
        print(n)


num = int(input("Enter number: "))
while num >= 0:
    print("You entered:", num)
    num = int(input("Enter number: "))


    word = input("Enter word: ")
for ch in word:
    if ch in "aeiouAEIOU":
        print(ch)


word = input("Enter word: ")
count = 0
for ch in word:
    if ch in "aeiouAEIOU":
        count += 1
print("Vowels:", count)


# SECTION:-5 Creative and Fun Loop Tasks:-
 
 
for i in range(5):
    print("Hello")


for i in range(3):
    color = input("Enter favorite color: ")
    print("You like", color)


for i in range(3):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()


word = "banana"
count = 0
for ch in word:
    if ch == 'a':
        count += 1
print("a appears", count, "times")


for i in range(1, 11):
    if i < 5:
        print(i, "Small")
    else:
        print(i, "Big")






