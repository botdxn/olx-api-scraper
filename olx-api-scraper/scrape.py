import requests
from bs4 import BeautifulSoup
import sys


# function to request and scrape ad data

def make_url(city: str, min_price: int, max_price: int) -> str:
    url_str = (
        "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/"
        + city
        + "/?search%5Bfilter_float_price%3Afrom%5D="
        + str(min_price)
        + "&search%5Bfilter_float_price%3Ato%5D="
        + str(max_price)
    )
    return url_str


def get_list_of_ads(url) -> list:

    list_of_ads = list()

    try:
        request_data = requests.get(url)
        soup = BeautifulSoup(request_data.content, "html.parser")
    except ConnectionError:
        sys.stdout.write(f"Connection error with {url}\n")

    try:
        content_div = soup.find("div", {"class": "content"})
        single_ads = content_div.find_all("div", {"class": "offer-wrapper"})
    except Exception:
        sys.stdout.write("Scraping error for divs containing data\n")

    for i, single_ad in enumerate(single_ads):
        ad_header = single_ad.find("h3", {"class": "lheight22 margintop5"})
        ad_title = ad_header.find("strong").text
        ad_href = ad_header.find("a")["href"]
        ad_price = single_ad.find("p", {"class": "price"})
        ad_price = ad_price.find("strong").text
        list_of_ads.append([i, ad_title, ad_href, ad_price])

    new_list_of_ads = [
        {"id": ad[0], "title": ad[1], "href": ad[2], "price": ad[3]}
        for ad in list_of_ads
    ]

    return new_list_of_ads


if __name__ == "__main__":
    print(get_list_of_ads(make_url("legnica", 500, 1000)))
