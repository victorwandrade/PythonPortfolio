#Day 2
#Tip Calculator
print ("Welcome to the tip calculator.")

total = float(input("What was the total bill? "))
people = int(input("How many people are splitting the bill? "))
percentage = int(input("What is the percentage you want to tip? 10, 12, 15 or 20?"))
percentage = 1 + percentage/100

total_with_tip = total * percentage

total_per_person = round(total_with_tip/people, 2)


print(f"Each person should pay a total amount of: {total_per_person:}")
