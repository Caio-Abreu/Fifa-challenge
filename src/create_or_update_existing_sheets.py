import os.path
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def create_or_update_existing_sheets(df):
    """Shows basic usage of the Sheets API.
    Updates an existing spreadsheet and adds a pandas DataFrame.
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        # The ID of your existing spreadsheet
        spreadsheet_id = os.getenv("SPREADSHEET_ID")

        if spreadsheet_id == "":
            # Create a new spreadsheet
            spreadsheet = {
                'properties': {
                    'title': "Challenge 1 - FIFA World Cup Finals"
                }
            }
            spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                        fields='spreadsheetId').execute()
            print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
            spreadsheet_id = spreadsheet.get('spreadsheetId')
        
        is_active = os.getenv("IS_ACTIVE")
        
        if is_active:
            # Convert the DataFrame to a list of lists and include the header
            values = [df.columns.tolist()] + df.values.tolist()

            # Calculate the range based on the size of the DataFrame
            range_ = f"Página1!A1:{chr(65 + len(df.columns))}{len(df) + 1}"

            body = {
                'values': values
            }
            result = service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=range_,
                valueInputOption="USER_ENTERED",
                body=body).execute()

            print('{0} cells updated.'.format(result.get('updatedCells')))

            print(f"New Spreadsheet created/update: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")
        else:
            print("The script is not active. Please set the IS_ACTIVE environment variable to True.")

    except HttpError as err:
        print(err)