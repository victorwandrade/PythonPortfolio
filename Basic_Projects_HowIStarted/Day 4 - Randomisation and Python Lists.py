#Day 4
#randomness
import random   #random module

"""
random_integer = random.randint(1,4)
print (random_integer)

random_float = random.random()
print (random_float)

print (random_float+random_integer)
#or
print(random_float*5)


love_score = random.randint(1,100)
print (f"your love score is {love_score}")
"""
"""
#Head of Tails

#Mine, you choose and then you get the result

choice = input("Choose one, Heads or Tails? ").lower()
numeric = 0
if choice == "heads":
    numeric = 0
    print ("you chose Heads!")
elif choice == "tails":
    numeric = 1
    print ("you chose Tails!")
else:
    print("Invalid Choice")

print("Let's toss the coin!")

random_side = random.randint(0,1)
if numeric == random_side and numeric == 0:
    print ("It is Heads! You won!")
elif numeric == random_side and numeric == 1:
    print ("It is Tails! You won!")
elif numeric != random_side and numeric == 0:
    print ("It is Tails! You Lost!")
else:
    print ("It is Heads, You Lost!")

#from the lecture... simpler:

print("let's toss a coin") 


if random_side == 0:
    print ("Heads!")
else:
    print ("Tails!")

"""
"""
#Banker Roulette
names_string = "Angela, Ben, Jenny, Michael, Chloe"

names = names_string.split(", ")

random_name = random.randint(0,len(names)-1)

print(f"{names[random_name]} is going to buy lunch today")
"""
"""
#treasure map
#### mine ######
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input().upper() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if int(position[1]) == 1:
    if position[0] == "A":
        line1[0] = "X"
    elif position[0] == "B":
        line1[1] = "X"
    else:
        line1[2]= "X"
elif int(position[1]) == 2:
    if position[0] == "A":
        line2[0] = "X"
    elif position[0] == "B":
        line2[1] = "X"
    else:
        line2[2]= "X"
else:
    if position[0] == "A":
        line3[0] = "X"
    elif position[0] == "B":
        line3[1] = "X"
    else:
        line3[2]= "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

#treasure map
#### hers ######
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1

map[number_index][letter_index] = "X"



# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

"""

"""
#Rock Paper Scisors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choice = int(input("choose your move: 0 for Rock; 1 for Paper; 2 for scisors: "))

if your_choice == 0:
    print("Your Choice:")
    print (rock)
elif your_choice == 1:
    print("Your Choice:")
    print (paper)
elif your_choice == 2:
    print("Your Choice:")
    print (scissors)
else:
    print ("Voce nao quer jogar, voce fala")

computer_choice = random.randint(0,2)

if computer_choice == 0:
    print("Computer's Choice:")
    print (rock)
elif computer_choice == 1:
    print("Computer's Choice:")
    print (paper)
elif computer_choice == 2:
    print("Computer's Choice:")
    print (scissors)

if your_choice == computer_choice:
    print ("That's a Draw! try again")
elif your_choice == 0 and computer_choice == 1:
    print ("You Lost! Computer Won! Paper beats Rock")
elif your_choice == 1 and computer_choice == 2:
    print ("You Lost! Computer Won! Scissors beats Paper")
elif your_choice == 2 and computer_choice == 0:
    print ("You Lost! Computer Won! Rock beats Scissors")
elif your_choice == 0 and computer_choice == 2:
    print ("You Won! Computer Lost! Rock beats Scissors")
elif your_choice == 1 and computer_choice == 0:
    print ("You Won! Computer Lost! Paper beats Rock")
elif your_choice == 2 and computer_choice == 1:
    print ("You Won! Computer Lost! Scissors beats Paper")
else:
    print ("Voce nao quer jogar. nao precisa nem falar")
"""

#ajudinha do bard pra fazer isso aqui um loopzinho
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    your_choice = input("Choose your move: 0 for Rock, 1 for Paper, 2 for Scissors, or type 'stop' to quit: ")

    if your_choice == "stop":
        break  # Exit the loop if "stop" is entered

    try:
        your_choice = int(your_choice)  # Attempt to convert input to integer

        if 0 <= your_choice <= 2:
            # Game logic here (same as your original code)
            print("Your Choice:")
            if your_choice == 0:
                print(rock)
            elif your_choice == 1:
                print(paper)
            else:
                print(scissors)

            computer_choice = random.randint(0, 2)
            print("Computer's Choice:")
            if computer_choice == 0:
                print(rock)
            elif computer_choice == 1:
                print(paper)
            else:
                print(scissors)

            # Determine the winner
            if your_choice == computer_choice:
                print("That's a Draw! Try again")
            elif (your_choice == 0 and computer_choice == 1) or (your_choice == 1 and computer_choice == 2) or (
                your_choice == 2 and computer_choice == 0
            ):
                print("You Lost! Computer Won!")
            else:
                print("You Won! Computer Lost!")
        else:
            print("Invalid input. Please enter 0, 1, 2, or 'stop'.")
    except ValueError:
        print("Invalid input. Please enter a number or 'stop'.")