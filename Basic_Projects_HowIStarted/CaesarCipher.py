alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keep_going = "yes"

def caesar(start_text, shift_amount, cypher_direction):
        end_text = ""
        if cypher_direction == "encode":
            for char in start_text:
                if char in alphabet:
                #dealing with cases of when number/symbol/space exist during the encoded/decoded proccess
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

#Import and print the logo from art.py when the program starts.
import art
print (art.logo)

while keep_going == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cypher_direction=direction)
    keep_going = (input("Wanna keep going? yes or no? "))
