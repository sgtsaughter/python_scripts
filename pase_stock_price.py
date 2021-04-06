import bs4
import requests
from bs4 import BeautifulSoup

# Get and parse stock price from finance.yahoo.com
def parse_price():
    r = requests.get('https://finance.yahoo.com/quote/sq?p=sq')
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price


while True:
    print('The current price is ' + str(parse_price()))

