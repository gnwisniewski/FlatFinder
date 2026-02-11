import requests
from bs4 import BeautifulSoup

def parseOlx(response: requests.Response):
    soup = BeautifulSoup(response.text, "html.parser")
    
    ads_json = []
    
    matching_ads = soup.select("div.css-j0t2x2")[0]
    ads = matching_ads.select("div.css-1sw7q4x")
    for ad in ads:
        titleTagParent = ad.select("a.css-1tqlkj0")[1]
        titleTag = titleTagParent.select("h4.css-hzlye5")[0]
        title = titleTag.text

        link = f"www.olx.pl/{titleTagParent.get('href')}"

        imageTagParent = ad.select("a.css-1tqlkj0")[0]
        imageTag = imageTagParent.select("img.css-8wsg1m")[0]
        imageUrl = imageTag.get("src")

        priceTag = ad.select("p.css-blr5zl")[0]
        price = ''.join(filter(str.isdigit, priceTag.text))

        notes = "xyz"

        ad_info = {
            "name": title,
            "link": link,
            "image_link": imageUrl,
            "price": price,
            "notes": notes
        }
        ads_json.append(ad_info)
    return ads_json

