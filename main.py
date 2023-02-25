"""
age = 20
price = 19.95
first_name = "Will"
is_online = False

name = input("What is your name? ")

print("Hello, " + name)
print(age)
print(price)

if is_online: print("True!")

birth_year = input("Enter your birth year: ")
age = 2023 - int(birth_year)
print("Your age is: " + str(age))
"""

'''
sum_1 = float(input("Enter a number: "))
sum_2 = float(input("Enter another number: "))
answer = sum_1 + sum_2
print(str(sum_1) + "+" + str(sum_2) + "=" + str(answer))
'''

"""
course = 'Python for Beginners'
print(course.replace('Beginners', 'Losers'))
print(course.find('y'))  # Expect 1 (second letter is y)
print('Python' in course)  # Expect true

print(10 / 3)  # Float
print(10 // 3)  # Int

# Augmented assignment operator:
x = 10
x += 3  # x is now == 13

# Logical operators
price = 25
print(10 < price < 30)  # Can also do price > 10 and price < 30
"""

"""
temp = 35
if temp > 30:
    print("It's hot!")
else:
    print("It's cold")
print("Also this line")
"""

'''
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight * 2.2
    print(str(weight) + " KG is equal to " + str(converted) + " lbs.")
else:
    converted = weight / 2.2
    print(str(weight) + " lbs is equal to " + str(converted) + " KG.")
'''

"""
i = 1
while i <= 5:
    print(i * '*')
    i += 1
while i >= 0:
    print(i * '*')
    i -= 1
"""

'''
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names[0:3])
print(names)
print(names[-1])
'''

"""
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, 999)
if 1 in numbers:
    print(numbers)
if 6 not in numbers:
    print("Ain't no 6")
print(len(numbers))

for i in numbers:
    print("* " + str(i))

i = 0
while(i < len(numbers)):
    print("* " + str(numbers[i]))
    i += 1
"""

'''
# Basic way:
numbers = range(5)
print(numbers)
for i in numbers:
    print(i)

# Simpler:
for i in range(5, 10, 2):
    print(i)
'''

# Tuples are immutable (cannot be changed)
numbers = (1, 2, 3, 2, 2)
print(numbers)
print("Count of 2: " + str(numbers.count(2)))
print("Index of first 3: " + str(numbers.index(2)))
