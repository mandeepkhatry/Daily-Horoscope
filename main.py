
from pick.pull import Scraper

def implement(horoscope):
    all=[]
    url = "https://www.astrology.com/horoscope/daily/" + horoscope.lower() +".html"
    scraper = Scraper(url)
    l = scraper.scrape()
    all.append(horoscope)
    all.append(l[0])
    all.append(l[1])
    return all

