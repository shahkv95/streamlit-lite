import bs4 as bs
import requests

def web_scrapper(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    read_url = requests.get(url, headers={'User-Agent': 'Custom'})
    income_soup = bs.BeautifulSoup(read_url.text, "lxml")
    return income_soup