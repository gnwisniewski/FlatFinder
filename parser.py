import requests
from bs4 import BeautifulSoup
from listings import Listing

def parseOtodom(response: requests.Response) -> list[Listing]:
    soup = BeautifulSoup(response.text, "html.parser")
    
    listings = []
    
    matching_ads = soup.select("div[data-cy='search.listing.organic']")[0]
    ads = matching_ads.select("ul section")
    for ad in ads[:-1]:
        titleTag = ad.select("p.css-135367.e11az2p02")[0]
        title = titleTag.text

        linkTag = ad.select("a.css-16vl3c1.e13tkx7i0")[0]
        link = f"www.otodom.pl/{linkTag.get('href')}"

        imageTag = ad.select("img.css-wmoe9r.enc9gby0")[0]
        imageUrl = imageTag.get("src")

        priceTag = ad.select("span.css-ussjv3.eanmlll1")[0]
        price = ''.join(filter(str.isdigit, priceTag.text))

        otherCosts = 0

        isRealtorListing = True

        notes = "xyz"

        listing = Listing(title, link, imageUrl, price, otherCosts, isRealtorListing, notes)
        listings.append(listing)

    return listings

def parseOlx(response: requests.Response) -> list[Listing]:
    soup = BeautifulSoup(response.text, "html.parser")
    
    listings = []
    
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

        otherCosts = 0

        isRealtorListing = True

        notes = "xyz"

        listing = Listing(title, link, imageUrl, price, otherCosts, isRealtorListing, notes)
        listings.append(listing)

    return listings

def parseTrojmiasto(response: requests.Response) -> list[Listing]:
    soup = BeautifulSoup(response.text, "html.parser")
    
    listings = []
    
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

        listing = Listing(title, link, imageUrl, price, otherCosts, isRealtorListing, notes)
        listings.append(listing)

    return listings