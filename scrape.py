from bs4 import BeautifulSoup
import requests, json

def get_list_of_ads(city: str, min_price: str, max_price: str):
    URL = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/' + str(city) + '/?search%5Bfilter_float_price%3Afrom%5D=' + str(min_price) + '&search%5Bfilter_float_price%3Ato%5D=' + str(max_price)
    
    list_of_ads = []
    
    request_data = requests.get(URL)
    soup = BeautifulSoup(request_data.content, 'html.parser')
    
    content_div = soup.find("div", {"class": "content"})
    single_ads = content_div.find_all("div", {"class": "offer-wrapper"})
    
    for i, single_ad in enumerate(single_ads):
        ad_header = single_ad.find("h3", {"class": "lheight22 margintop5"})
        ad_title = ad_header.find("strong").text
        ad_href = ad_header.find("a")['href']
        ad_price = single_ad.find("p", {"class": "price"})
        ad_price = ad_price.find("strong").text
        
        list_of_ads.append([i, ad_title, ad_href, ad_price]) 
        
    dict_of_ads = [{'id': ad[0], 'title': ad[1], 'href': ad[2], 'price': ad[3]} for ad in list_of_ads]
        
    return dict_of_ads