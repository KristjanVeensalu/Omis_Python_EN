import requests
from bs4 import BeautifulSoup
URL = 'https://www.facebook.com/GurenZify/friends?lst=100001843291975%3A100001843291975%3A1592497122&source_ref=pb_friends_tl'

fetchedData = requests.get(URL)

soup = BeautifulSoup(fetchedData.content, 'html.parser')

print(soup.prettify())