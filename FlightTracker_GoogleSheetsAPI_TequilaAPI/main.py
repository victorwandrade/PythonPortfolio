#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

EMAIL = "Enter your Email here"


TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "Enter your TequilaAPIKey"


data_manager = DataManager()
sheet_data = data_manager.get_sheet_data() #getting the information from the google sheets
#print(sheet_data)

cities = [sheet_data['prices'][i]['City'] for i in range(0,9)]


flight_search = FlightSearch(sheet_data["prices"]) #updating the blank IATA CODE cells with "TESTING"
modified_data = flight_search.generate_IATA()
formatted_data = flight_search.get_formatted_data()
data_manager.update_sheet_data(formatted_data)  #UPDATING THE GOOGLE SHEET

flight_price = FlightData(formatted_data)
prices = flight_price.find_price()

for key, value in prices.items():
    print(f"{key}: {value}")
    
print (modified_data) 
print (prices)

for city, price in prices.items():
    for data_item in modified_data:
        if data_item['City'] == city:
            lowest_price = data_item['Lowest Price']
            # Check data types before conversion
            try:
                price = int(price)  # Convert price to integer
                lowest_price = int(lowest_price)  # Convert lowest_price to integer
            except ValueError:
                print(f"Error converting price or lowest_price for {city}")
                continue  # Skip this city if conversion fails
            if price < lowest_price:
                notification_manager = NotificationManager(EMAIL)  # Pass the same email as used above
                notification_manager.send_email(city, price, lowest_price)
                break  # Send email only once per city
            else:
                print(f"Price for {city} is not a deal. Current price: {price}, lowest recorded price: {lowest_price}")



