import requests, schedule
from config import queries, headers
from urllib.parse import urlparse
from trojmiasto import parseTrojmiasto

def main():
    print("Starting FlatFinder...")
    for query in queries:
        response = requests.get(query, headers=headers)
        if response.ok:
            domain  = urlparse(query).netloc
            print(f"Successfully fetched data from {domain}")
            
            if domain == "ogloszenia.trojmiasto.pl":
                parseTrojmiasto(response)
            elif domain == "www.otodom.pl":
                pass
            elif domain == "www.olx.pl":
                pass
            else:
                print("Website not supported.")
        else:
            print(f"Failed to fetch data from {query} with status code {response.status_code}")

if __name__ == "__main__":
    main()