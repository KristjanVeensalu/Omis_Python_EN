import requests
from bs4 import BeautifulSoup
URL = 'graph.facebook.com'

fetchedData = requests.get(URL)

soup = BeautifulSoup(fetchedData.content, 'html.parser')

print(soup.prettify())