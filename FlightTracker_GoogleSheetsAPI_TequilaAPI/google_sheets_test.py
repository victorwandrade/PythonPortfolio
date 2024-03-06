import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "Enter your Spreadsheet ID"
RANGE_NAME = "The Range you want to work on"

def _setup_credentials():
    """
    Sets up authorization credentials for accessing the Google Sheet.
    """
        
    if os.path.exists("token.json"):
        return Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
        return credentials

credentials = _setup_credentials()
service = build("sheets", "v4", credentials=credentials)

def get_sheet_data():
    """
    Retrieves data from the specified Google Sheet and returns it as a structured dictionary.
    """
    try:
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get("values", [])

        if not values:
            raise ValueError("No data found in the specified range of the spreadsheet.")

        headers = values[0]
        data = {
            "dados": [
                {header: row[i] for i, header in enumerate(headers)}
                for row in values[1:]  # Skip the header row
            ]
        }
        return data
    except HttpError as error:
        raise ValueError(f"An error occurred while retrieving data from the Google Sheet: {error}")

def update_sheet_data(data):
    """
    Updates specific cells in the Google Sheet with the provided data.

    Args:
        data: A list of tuples, where each tuple represents a cell update:
            (row_number, column_index, value)

    Returns:
         None
    """
    try:
        body = {"values": data}
        sheets = service.spreadsheets()
        sheets.values().update(
        spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
        valueInputOption="USER_ENTERED", body=body
        ).execute()
        print("Sheet updated successfully!")
    except HttpError as error:
        raise ValueError(f"An error occurred while updating the Google Sheet: {error}")
    
    
sheet_data = get_sheet_data()

print(sheet_data)