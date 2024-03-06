import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "Enter your TequilaAPIKey" #header

class FlightSearch:

    def __init__(self, data):
        self.data = data

    def generate_IATA(self):
        """
        Modifies the `data` attribute, replacing empty IATA codes with the actual IATACODE.

        Returns:
            A list of dictionaries with the updated IATA codes.
        """

        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}

        city_to_code_map = {}  # Create an empty map for efficiency
        for item in self.data:
            city = item["City"]
            if city not in city_to_code_map:
                query = {"term": city, "location_types": "city"}
                response = requests.get(url=location_endpoint, headers=headers, params=query)
                response.raise_for_status()
                try:
                    code = response.json()["locations"][0]["code"]
                    city_to_code_map[city] = code
                except (IndexError, KeyError):
                    print(f"Warning: IATA code not found for {city}")
                    continue

            item["IATA Code"] = city_to_code_map[city]

        return self.data

    def get_formatted_data(self):
        """
        Returns the `data` attribute as a list of dictionaries with header row.

        Returns:
            A list of lists representing the formatted data.
        """

        rows = [["City", "IATA Code", "Lowest Price"]]  # Add header row
        for item in self.data:
            rows.append([item["City"], item["IATA Code"], item["Lowest Price"]])

        return rows