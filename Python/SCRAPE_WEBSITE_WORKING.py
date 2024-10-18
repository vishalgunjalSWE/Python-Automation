# In DevOps, it is used for log analysis/processing
# Ensure you have the necessary libraries installed:
# pip install beautifulsoup4 requests

import urllib.request
from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        try:
            # Fetching the HTML content of the site
            response = requests.get(self.site)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Parsing the HTML content
            parser = "html.parser"
            sp = BeautifulSoup(response.content, parser)
            print(sp.prettify())  # Print prettified HTML
            
            # Finding all anchor tags and filtering URLs
            print("\nFiltered URLs:")
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url and "articles" in url:  # Check if 'articles' is in the URL
                    print(url)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching the site: {e}")


# Specify the news website to scrape
news_site = "https://google.com"
Scraper(news_site).scrape()


# Creating a simple class to demonstrate class usage
class Cloud:
    def __init__(self, value):
        self.value = value

    # Method inside the class
    def hello(self):
        print(self.value)


# Calling the class with a method
test_message = "DevOps a gaya"
Cloud(test_message).hello()
