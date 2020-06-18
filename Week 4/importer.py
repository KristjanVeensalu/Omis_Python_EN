import requests
from bs4 import BeautifulSoup
URL = 'https://www.facebook.com/'

fetchedData = requests.get(URL)

soup = BeautifulSoup(fetchedData.content, 'html.parser')

print(soup)