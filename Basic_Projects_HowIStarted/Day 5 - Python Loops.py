#day 5
"""
# Input a Python list of student heights

student_heights = [151,145,179]
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
number_of_students = 0
for n in student_heights:
    total_height = n + total_height
    number_of_students += 1

print (f"total height is: {total_height}")
print (f"total number of students is: {number_of_students}")
print (f"average height is: {int(total_height/number_of_students)}")
"""
"""
#FizzBuzz Game
#For Loops with range function
target = 100
for number in range (1, target+1):
  if number % 3 == 0 and number % 5 == 0:
    print ("FizzBuzz")
  elif number % 3 == 0:
    print ("Fizz")
  elif number % 5 == 0:
    print ("Buzz")
  else:
    print (number)
"""

#### Final Project ####
#### Password Generator ####
#### I did with While Loops ####

import string
import random

alphabet = string.ascii_letters
letters = []
for letter in alphabet:
    letters.append(letter)

digits = string.digits
numbers = []
for number in digits:
    numbers.append(number)

printable = string.printable
symbols = [char for char in printable if char not in alphabet and char not in digits]

"""
#easy version: person chooses how many letters, numbers and symbols and gets them placed in order to get the password


number_of_letters = int(input("How many letters you want in your password? "))
number_of_numbers = int(input("How many numbers you want in your password? "))
number_of_symbols = int(input("How many symbols you want in your password? "))

password = ""
count = 0
while count < number_of_letters:
    random_number = random.randint(0, len(letters-1))
    password = password + letters[random_number]
    count += 1

count = 0
while count < number_of_numbers:
    random_number = random.randint(0, len(numbers)-1)
    password = password + numbers[random_number]
    count += 1

count = 0
while count < number_of_symbols:
    random_number = random.randint(0, len(symbols)-1)
    password = password + symbols[random_number]
    count += 1

print (f"Your random password is: {password}")
"""

#hard version: after person chooses how many letters, numbers and symbols; it needs to generate a random password out of line
number_of_letters = int(input("How many letters you want in your password? "))
number_of_numbers = int(input("How many numbers you want in your password? "))
number_of_symbols = int(input("How many symbols you want in your password? "))
password_lenght = number_of_letters + number_of_numbers + number_of_symbols

password = ""

while password_lenght > 0:
    random_number1 = random.randint(1, 3)

    if random_number1 == 1:
        while number_of_letters > 0:
          random_number = random.randint(0, len(letters)-1)
          password = password + letters[random_number]
          number_of_letters -= 1
          password_lenght -= 1
          break

    elif random_number1 == 2:
        while number_of_numbers > 0:
          random_number = random.randint(0, len(numbers)-1)
          password = password + numbers[random_number]
          number_of_numbers -= 1
          password_lenght -= 1
          break

    else:
        while number_of_symbols > 0:
          random_number = random.randint(0, len(symbols)-1)
          password = password + symbols[random_number]
          number_of_symbols -= 1
          password_lenght -= 1
          break


print (f"Your random password is: {password}")


#### Her solution with For Loops ####

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
