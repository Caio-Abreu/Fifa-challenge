# FIFA World Cup Data Scraper

This project scrapes data from the Wikipedia page for FIFA World Cup finals and updates a Google Sheets document with the data.

## Files

- `main.py`: The main script that calls the other functions.
- `src/scrape_wiki_fifa_finals.py`: Contains the `scrape_wiki_fifa_finals()` function that scrapes data from the Wikipedia page for FIFA World Cup finals and returns a pandas DataFrame.
- `src/create_or_update_existing_sheets.py`: Contains the `create_or_update_existing_sheets(df)` function that updates a Google Sheets document with the data from a pandas DataFrame.

## How to Run

1. Set the `SPREADSHEET_ID` environment variable to the ID of your Google Sheets document. If this variable is not set, a new Google Sheets document will be created.
2. Set the `IS_ACTIVE` environment variable to activate or deactivate the fill of text in spreadsheet.
3. Run `main.py`.

## Requirements

- Python 3.6 or higher
- pandas
- BeautifulSoup
- google-auth
- google-auth-httplib2
- google-auth-oauthlib
- google-api-python-client
- oauthlib