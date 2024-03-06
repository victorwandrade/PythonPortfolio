import random   #random module
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

    your_choice = int(your_choice)  # Attempt to convert input to integer

    if 0 <= your_choice <= 2:
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
            print("That's a Draw! Go Again")
        elif (your_choice == 0 and computer_choice == 1) or (your_choice == 1 and computer_choice == 2) or (your_choice == 2 and computer_choice == 0):
            print("You Lost! Computer Won!")
        else:
            print("You Won! Computer Lost!")
    else:
        print("Invalid input. Please enter 0, 1, 2, or 'stop'.")
