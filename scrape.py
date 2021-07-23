from bs4 import BeautifulSoup
import requests

def get_list_of_ads(city, min, max):
    URL = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/' + city + '/?search%5Bfilter_float_price%3Afrom%5D=' + min + '&search%5Bfilter_float_price%3Ato%5D=' + max
    
    