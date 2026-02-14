import pandas as pd
from dataclasses import dataclass, asdict
from typing import Optional
from pathlib import Path

FILENAME = "listings.xlsx"

@dataclass
class Listing:
    name: str
    link: str
    image_link: str
    price: int
    other_costs: int
    is_realtor: bool
    notes: Optional[str] = None

def syncListings(scrapped_listings: list[Listing]):
    try:
        df_saved = pd.read_excel(FILENAME)
        saved_listings = {row["link"]: row for _, row in df_saved.iterrows()}
    except FileNotFoundError:
        saved_listings = {}

    scrapped_dict = {listing.link: listing for listing in scrapped_listings}

    final_listings = []

    for link, saved in saved_listings.items():
        if link in scrapped_dict:
            scrapped = scrapped_dict[link]
            
            if int(scrapped.price) != int(saved["price"]) or int(scrapped.other_costs) != int(saved["other_costs"]):
                print(f"Price/other costs changed for {link}: {saved['price']} -> {scrapped.price}")

            final_listings.append(asdict(scrapped))  
            del scrapped_dict[link]
        else:
            print(f"Listing no longer active, removing: {link}")

    for link, new_listing in scrapped_dict.items():
        print(f"New listing found: {link}")
        final_listings.append(asdict(new_listing))    

    
    df_final = pd.DataFrame(final_listings)
    df_final.to_excel(FILENAME, index=False)
    print(f"Excel updated with {len(final_listings)} listings")
