import requests
from config import queries, headers
from urllib.parse import urlparse
from trojmiasto import parseTrojmiasto
from olx import parseOlx

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    print("Starting FlatFinder...")
    for query in queries:
        response = requests.get(query, headers=headers)
        if response.ok:
            domain  = urlparse(query).netloc
            
            if domain == "ogloszenia.trojmiasto.pl":
                parseTrojmiasto(response)
            elif domain == "www.otodom.pl":
                pass
            elif domain == "www.olx.pl":
                parseOlx(response)
            else:
                print("Website not supported.")
        else:
            print(f"Failed to fetch data from {query} with status code {response.status_code}")

if __name__ == "__main__":
    main()