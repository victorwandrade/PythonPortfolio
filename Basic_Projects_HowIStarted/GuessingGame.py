import random
def difficulty():
    difficulty = input("Choose your Difficulty level: easy, medium or hard? ").lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "medium":
        attempts = 7
    elif difficulty == "hard":
        attempts = 5
    else:
        print ("Invalid choice")
    return attempts

def guessing_game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    
    randomnumber = random.choice(range(1,100))
    #print (f"testing... answer is {randomnumber}")
    
    attempts = difficulty()
        
    print (f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    while attempts > 0:
        if guess == randomnumber:
            print (f"You got it! The answer was {guess}")
            break
        
        else:
            if guess > randomnumber:
                attempts -= 1
                if attempts == 0:
                    print ("You've run out of guesses, you lose.")
                    break
                print (f"Too High! \nGuess again \nYou have {attempts} attempts remaining to guess the number.")
                
            elif guess < randomnumber:
                attempts -= 1
                if attempts == 0:
                    print ("You've run out of guesses, you lose.")
                    break
                print (f"Too Low! \nGuess again \nYou have {attempts} attempts remaining to guess the number.")
                
        guess = int(input("Make a guess: "))
        
    again = input("wanna go again? y or n? ")
    if again == "y":
        guessing_game()
    else:
        print ("Thanks for playing!")
        
            
guessing_game()
