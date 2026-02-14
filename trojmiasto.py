import requests
from bs4 import BeautifulSoup

def parseTrojmiasto(response: requests.Response):
    soup = BeautifulSoup(response.text, "html.parser")
    
    ads_json = []
    
    ads = soup.select("div.list__item")
    for ad in ads:
        titleTag = ad.select("h2.list__item__content__title a")[0]
        title = titleTag.get("title")

        link = titleTag.get("href")

        firstImageTag = ad.select("a.listItemFirstPhoto img")[0]
        imageUrl = firstImageTag.get("src") 

        priceTag = ad.select("p.list__item__price__value span")[0]
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
        ads_json.append(ad_info)
    return ads_json

