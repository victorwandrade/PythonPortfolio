#Day 13 - Debugging: How to Find and Fix Errors in your Code
############DEBUGGING#####################

# # Describe Problem
#def my_function():
#   for i in range(1, 20): # just need to change 20 to 21.
#      if i == 20:
#           print("You got it")
#my_function()

# Reproduce the Bug
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
##dice_num = randint(1,6)  # list goes from 0 to 5
#dice_num = randint(0, 5)  #fixed
#print(dice_imgs[dice_num])


## Play Computer
#year = int(input("What's your year of birth?"))
#if year > 1980 and year < 1994:   #if we put 1994 it will skip both conditions... fix by including '='in one of them
#   print("You are a millenial.")
##elif year > 1994:
#elif year >= 1994: # -> fixed
#   print("You are a Gen Z.")

## Fix the Errors
#age = int(input("How old are you?"))
#if age > 18:
#    print(f"You can drive at age {age}.")

#Print is Your Friend
#pages = 0
#word_per_page = 0
#pages = int(input("Number of pages: "))
##word_per_page == int(input("Number of words per page: ")) # == wont work
#word_per_page = int(input("Number of words per page: "))
#total_words = pages * word_per_page
#print(total_words)

##Use a Debugger
#def mutate(a_list):
#  b_list = []
#  for item in a_list:
#    new_item = item * 2
#    b_list.append(new_item)
#  print(b_list)

#mutate([1,2,3,5,8,13])

#Fixing bugs 
#number = int(input("Which number do you want to check? ")) # Which number do you want to check?

#if number % 2 == 0:   #missing an '='
#  print("This is an even number.")
#else:
#  print("This is an odd number.")


# Which year do you want to check?
#year = int(input("# Which year do you want to check? "))  #Just had to add int

#if year % 4 == 0:
#  if year % 100 == 0:
#    if year % 400 == 0:
#      print("Leap year.")
#    else:
#      print("Not leap year.")
#  else:
#    print("Leap year.")
#else:
#  print("Not leap year.")

target = int(input("What's your target? "))
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:  #and not or
    print("FizzBuzz")
  elif number % 3 == 0:  # elif not if
    print("Fizz")
  elif number % 5 == 0: # elif not if
    print("Buzz")
  else:
    print(number)  # remove []