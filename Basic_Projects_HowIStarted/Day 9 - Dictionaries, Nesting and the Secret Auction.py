#Day 9 - Dictionaries and Nesting

"""
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again.",
                          }

#Retrieving items from dictionary.
print (programming_dictionary["Bug"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existind dictionary
#programming_dictionary = {}

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

"""
"""
#grading problem
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.

# TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = {}
for name in student_scores:
    if student_scores[name] < 70:
        student_grades[name] = "Fail"
    elif student_scores[name] in range (71,80):
        student_grades[name] = "Acceptable"
    elif student_scores[name] in range (81,90):
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name] > 90:
        student_grades[name] = "Outstanding"
    
#hers:
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

"""
"""
#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a Dictionary and dictionary in a dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],"total number of visits": 12}, 
    "Germany": {"cities visited":["Berlin", "Hamburg", "Stuttgart"],"total number of visits": 5},
    }

#Nexting Dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total number of visits": 12
        }, 
    {
        "country":"Germany",
        "cities visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total number of visits": 5
        },
    ]

print(travel_log )

"""
"""
#Dictionary in List Exercise

country = input("Add country name: ") # Add country name
visits = int(input("Number of visits: ")) # Number of visits
list_of_cities = eval(input("create list from formatted string ")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(name, times_visited, cities_visited):
    travel_log.append({
    "country": name,
    "visits": times_visited,
    "cities": cities_visited
    })

#or
# hers
def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
    
# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
print (travel_log)
"""

#Auction bid exercise
#mine
from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
auction_dic = {}
bidding = True


def blind_auction():
    highest_bid = 0
    winner = ""
    for bidder in auction_dic:
    bid = auction_dic[bidder]
    winner = bidder
    if bid > highest_bid:
        highest_bid = bid
        winner = bidder
    print (f"the winner is {winner} with a bid of R$ {highest_bid}")

  
    while bidding == True:
        name = input("What is your name? ")
        bid = float(input("What is your bid? R$ "))
        auction_dic[name] = bid
        more = input("Are there any other bidders? yes or no? ").lower()
        if more == "no":
            clear()
            bidding = False
        else:
            clear()

blind_auction()




#hers

from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  

