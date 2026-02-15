import time
import requests
import schedule
from config import queries, headers
from urllib.parse import urlparse
from parser import parseOlx, parseOtodom, parseTrojmiasto
from listings import syncListings

def scheduler():
    print("Starting FlatFinder scheduler...")
    main()

    schedule.every(5).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
def main():
    print("Starting scraping...")
    active_listings = []
    for query in queries:
        response = requests.get(query, headers=headers)
        if response.ok:
            domain = urlparse(query).netloc

            if domain == "ogloszenia.trojmiasto.pl":
                active_listings.extend(parseTrojmiasto(response))
            elif domain == "www.otodom.pl":
                active_listings.extend(parseOtodom(response))
            elif domain == "www.olx.pl":
                active_listings.extend(parseOlx(response))
            else:
                print("Website not supported.")
        else:
            print(f"Failed to fetch data from {query} with status code {response.status_code}")

    syncListings(active_listings)

if __name__ == "__main__":
    scheduler()