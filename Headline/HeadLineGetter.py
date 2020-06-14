#https://newsapi.org/
from yfinance import Ticker


class HeadlineGetter:
    def HeadlineGetter():
        msft = yf.Ticker("MSFT")
        print(msft.info)