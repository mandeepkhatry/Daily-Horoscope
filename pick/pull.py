
import requests

from bs4 import BeautifulSoup


class Scraper:
    def __init__(self,url):
        self.url=url


    def scrape(self):

        l=[]
        response= requests.get(self.url)

        html= response.text

        soup = BeautifulSoup(html, 'html.parser')

        date = soup.find('span', class_="page-horoscope-date-font")

        date = date.text

        post = soup.find(class_="page-horoscope-text")

        post = post.text

        l.append(date)
        l.append(post)

        return l

