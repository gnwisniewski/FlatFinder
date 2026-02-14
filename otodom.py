import requests
from bs4 import BeautifulSoup

def parseOtodom(response: requests.Response):
    soup = BeautifulSoup(response.text, "html.parser")
    
    ads_json = []
    
    matching_ads = soup.select("div[data-cy='search.listing.organic']")[0]
    ads = matching_ads.select("ul section")
    for ad in ads:
        titleTag = ad.select("p.css-135367.e11az2p02")[0]
        title = titleTag.text

        linkTag = ad.select("a.css-16vl3c1.e13tkx7i0")[0]
        link = f"www.otodom.pl/{linkTag.get("href")}"

        imageTag = ad.select("img.css-wmoe9r.enc9gby0")[0]
        imageUrl = imageTag.get("src")

        priceTag = ad.select("span.css-ussjv3.eanmlll1")[0]
        price = ''.join(filter(str.isdigit, priceTag.text))

        otherCosts = 0

        isRealtorListing = True

        notes = "xyz"

        ad_info = {
            "name": title,
            "link": link,
            "image_link": imageUrl,
            "price": price,
            "other_costs": otherCosts,
            "is_realtor": isRealtorListing,
            "notes": notes
        }
        print(ad_info)
        ads_json.append(ad_info)
    return ads_json

