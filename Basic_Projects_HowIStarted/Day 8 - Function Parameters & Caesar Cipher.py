#Day 8 - Function Parameters & Caesar Cipher
"""
# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    for x in range(0,10):
        print (x)
        if x == 5:
            print("How you doing?")
    print ("That's the end of this")
    
greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print (f"How do you do {name}?")
    
greet_with_name("Victor")




def greet_with(name, location):    #this definition can be positional or keyword
    print (f"Hello {name}")
    print (f"How is it like in {location} ?")
    
greet_with (location = "Franca", name ="Victor" )

"""
"""
# figuring out how much paint we will need
# Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    cans = (height*width)/cover
    print(f"you will need {math.ceil(cans)} cans to paint your wall")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("What's the height? ")) # Height of wall (m)
test_w = int(input("What's the width? ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


"""
"""

#Prime Number Checker

# Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for x in range (2,number):
        if number % x == 0:
            is_prime = False
    if is_prime:
        print ("It's a prime number")
    else:
        print ("It's not a prime number")
            



# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("insert a number ")) # Check this number
prime_checker(number=n)

"""

#Caesar Cipher:
"""
##### Step 1 - Encode
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    cypher_text = ""
    for letter in plain_text:
        index = alphabet.index(letter)
        new_index = (index + shift_amount) % len(alphabet)
        new_letter = alphabet[new_index]
        cypher_text = cypher_text + new_letter
    print (f"The encoded text is: {cypher_text}")
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
            
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(plain_text = text, shift_amount = shift)
"""
"""
##### Step 2 - Decode
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(cypher_text, shift_amount):
    plain_text = ""
    for letter in cypher_text:
        index = alphabet.index(letter)
        new_index = (index - shift_amount) % len(alphabet)
        new_letter = alphabet[new_index]
        plain_text = plain_text + new_letter
    print (f"The dencoded text is: {plain_text}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cypher_text=text,shift_amount = shift)
else:
    print ("not valid, write 'encode' to encrypt or 'decode' to decrypt")
    
"""   
""" 
##### Step 3 - Combine
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(start_text, shift_amount, cypher_direction):
        end_text = ""
        if cypher_direction == "encode":
            for letter in start_text:
                index = alphabet.index(letter)
                new_index = (index + shift_amount) % len(alphabet)
                new_letter = alphabet[new_index]
                end_text = end_text + new_letter
        elif direction == "decode":
            for letter in start_text:
                index = alphabet.index(letter)
                new_index = (index - shift_amount) % len(alphabet)
                new_letter = alphabet[new_index]
                end_text = end_text + new_letter
        print (f"Here is the {direction}d message: {end_text}")
        

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cypher_direction=direction)
""" 
#### Step 4 - Clean up
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keep_going = "yes"


def caesar(start_text, shift_amount, cypher_direction):
        end_text = ""
        if cypher_direction == "encode":
            for char in start_text:
                if char in alphabet:
                #TODO-3: What happens if the user enters a number/symbol/space?
                #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
                #e.g. start_text = "meet me at 3"
                #end_text = "•••• •• •• 3"
                    index = alphabet.index(char)
                    new_index = (index + shift_amount) % len(alphabet)
                    new_char = alphabet[new_index]
                    end_text = end_text + new_char
                else:
                    end_text += char
        elif direction == "decode":
            for char in start_text:
                if char in alphabet:
                    index = alphabet.index(char)
                    new_index = (index - shift_amount) % len(alphabet)
                    new_char = alphabet[new_index]
                    end_text = end_text + new_char
                else:
                    end_text += char
        print (f"Here is the {direction}d message: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
import art
print (art.logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
while keep_going == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).

    caesar(start_text=text, shift_amount=shift, cypher_direction=direction)
    keep_going = (input("Wanna keep going? yes or no? "))