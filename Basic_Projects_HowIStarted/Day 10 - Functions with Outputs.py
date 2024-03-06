#Day 10 - Functions with Outputs
"""
#name exercise
def format_name(f_name, l_name):
    "" #Take a first and last name and format it # (incluse one ' " ' to make this is a docstring... it is used to explain what is indice the program
    #to return the title case version of the name ""
    if f_name == "" and l_name == "":
        return "Your didn't provide valid inputs."
         
    first_name = (f_name).title()
    last_name = (l_name).title()
    
    return f"Result: {first_name} {last_name}" #most important line
    
formatado = format_name(input("What is your first name? "), input("What is your last name? "))
print (formatado)
"""

"""
#Leap year Exercise
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
    if is_leap(year) == False:
        month_days_notleap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days_notleap[month - 1]
    else:
        month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days_leap[month - 1] 
    
# Hers
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: ")) # Enter a year
month = int(input("Enter a month: ")) # Enter a month
days = days_in_month(year, month)
print(days)
"""


######   Calculator Project

from calculator_art import logo

#Add
def add (n1, n2):
    return float(n1 + n2)

#Subtract
def subtract (n1, n2):
    return float(n1 - n2)

#Multiply
def multiply (n1, n2):
    return float(n1 * n2)

#Divide
def divide (n1, n2):
    return float(n1 / n2)

operations  = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print (logo)
    
    
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print (symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print (f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
            
            
calculator()