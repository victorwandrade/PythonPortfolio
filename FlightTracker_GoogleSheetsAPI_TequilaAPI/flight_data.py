import requests
import datetime as dt

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "Enter your TequilaAPIKey" #this is a Header
ORIGIN_IATA = "Enter the IATA code from the city you want to fly from"
NOW = dt.datetime.now().strftime('%d/%m/%Y')
SIX_MONTHS = (dt.datetime.now() + dt.timedelta(days=180)).strftime('%d/%m/%Y')  #You will check for deals in the next 6 months
RETURN_MIN = (dt.datetime.now() + dt.timedelta(days=7)).strftime('%d/%m/%Y') #It is currently set for a min stay of 7 days
RETURN_MAX = (dt.datetime.now() + dt.timedelta(days=28)).strftime('%d/%m/%Y') #It is currently set for a max stay of 28 days


class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self, data):
        self.data = data
        
    def find_price(self):
        location_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        compil ={}
        for item in self.data[1:]:
            city = item[0]
            code = item[1]
            query = {
                "fly_from": ORIGIN_IATA, 
                "fly_to": code,
                "date_from":NOW,
                "date_to":SIX_MONTHS,
                "return_from":RETURN_MIN,
                "return_to":RETURN_MAX,                    
                "curr": "BRL",  #The currency you want to work on. you can get more information on the tequila API website
                "one_for_city": 1,
                "max_stopovers": 0,
                "limit":1
                }
            response = requests.get(url=location_endpoint, headers=headers, params=query)
            response.raise_for_status()
            data=response.json()['data'][0]['price']
            compil[city] = f"{data}"
            
        return compil