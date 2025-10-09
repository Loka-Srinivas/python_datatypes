# 21/08/2025
# MODULES INTRO AND RANDOM MODULE:-

# Generate a random float between 0.0 and 1.0.

import random

num = random.random()
print("Random float:", num)


# Generate a random integer between 1 and 100.

import random

num = random.randint(1,100)
print("Random integer:", num)


#Pick a random fruit from a list ["apple", "banana", "mango", "orange"]

import random

fruits = ["apple", "banana", "mango", "orange"]
choice = random.choice(fruits)
print("Random fruit:", choice)


#Shuffle a list of numbers [1,2,3,4,5].

import random

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)


#Generate 5 random integers between 10 and 50.

import random

nums = [random.randint(10, 50) for i in range(5)]
print("Random integers:", nums)
