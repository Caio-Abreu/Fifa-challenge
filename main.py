from src.scrape_wiki_fifa_finals import scrape_wiki_fifa_finals
from src.create_or_update_existing_sheets import create_or_update_existing_sheets

def main():
    df = scrape_wiki_fifa_finals()
    create_or_update_existing_sheets(df)

if __name__ == "__main__":
    main()