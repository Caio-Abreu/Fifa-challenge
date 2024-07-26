import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_wiki_fifa_finals():
    """
    Scrape the Wikipedia page for FIFA World Cup finals and return the data as a DataFrame.

    This function sends a GET request to the Wikipedia page, parses the HTML content to find the table with class 'plainrowheaders',
    extracts the headers and the data for the first 10 rows, and converts this data into a DataFrame.

    Returns:
        df (pandas.DataFrame): A DataFrame containing the year, winner, score, and runner-up for the first 10 FIFA World Cup finals.
    """
    # Send a GET request
    response = requests.get('https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals')

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'class': 'plainrowheaders'})

    # Find all rows in the table
    rows = table.find_all('tr')

    # Extract headers
    headers = [header.text.strip() for header in rows[0].find_all('th')]

    # Map headers to their index
    header_indices = {header: index for index, header in enumerate(headers)}

    # Iterate over the first 10 rows and find all columns
    data = []
    for row in rows[1:11]:  # Skip the header row
        cols = row.find_all(['td', 'th'])
        
        # Extract the text from the desired columns
        year = int(cols[header_indices['Year']].text.strip())
        winner = cols[header_indices['Winners']].text.strip()
        score = cols[header_indices['Score']].text.strip()
        runner = cols[header_indices['Runners-up']].text.strip()
        
        data.append([year, winner, score, runner])

    # Convert the list into a DataFrame
    df = pd.DataFrame(data, columns=['Year', 'Winner', 'Score', 'Runner-up'])
    
    print(df)

    return df