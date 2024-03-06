def tip_calculator(percentage):
    total = int(input("how much was the total bill? "))
    people = int(input("how many people are splitting the bill? "))
    percentage = int(input("whats the percentage you want to give? 10, 12, 15, 20? "))
    
    total_with_tip = total * (1 + percentage/100)
    print (f"Each person should pay: {total_with_tip/people}")

tip_percentage = int(input("whats the percentage you want to tip? enter as a whole number (Example: 10 for 10%): "))
tip_calculator(tip_percentage)
